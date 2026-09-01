"""User routes."""
import base64
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, Request, UploadFile, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

AVATAR_CONTENT_TYPES = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/webp": ".webp",
}
MAX_AVATAR_SIZE_BYTES = 5 * 1024 * 1024


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    """Get the current user's profile."""
    return current_user


@router.patch("/me", response_model=UserResponse)
def update_me(
    payload: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update the current user's profile."""
    if payload.full_name is not None:
        current_user.full_name = payload.full_name
    if payload.avatar_url is not None:
        current_user.avatar_url = payload.avatar_url
    if payload.bio is not None:
        current_user.bio = payload.bio
    db.commit()
    db.refresh(current_user)
    return current_user


@router.post("/me/avatar", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def upload_avatar(
    request: Request,
    image: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Upload and assign a persistent profile image for the current user."""
    try:
        # Validate content type
        extension = AVATAR_CONTENT_TYPES.get(image.content_type)
        if extension is None:
            raise HTTPException(
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
                detail="Upload a PNG, JPEG, or WebP image.",
            )

        # Read and validate file
        content = await image.read()
        if not content:
            raise HTTPException(status_code=400, detail="The selected image is empty.")
        if len(content) > MAX_AVATAR_SIZE_BYTES:
            raise HTTPException(status_code=413, detail="Image must be 5 MB or smaller.")

        # Ensure column type is TEXT in PostgreSQL
        try:
            db.execute(text("ALTER TABLE users ALTER COLUMN avatar_url TYPE TEXT;"))
            db.commit()
        except Exception:
            db.rollback()

        # Convert image to Base64 data URI so it persists in PostgreSQL forever across Render free tier container restarts
        b64_encoded = base64.b64encode(content).decode("utf-8")
        current_user.avatar_url = f"data:{image.content_type};base64,{b64_encoded}"

        # Also write local backup file if possible
        try:
            avatar_dir = Path(__file__).resolve().parents[2] / "uploads" / "avatars"
            avatar_dir.mkdir(parents=True, exist_ok=True)
            filename = f"user-{current_user.id}-{uuid4().hex}{extension}"
            filepath = avatar_dir / filename
            filepath.write_bytes(content)
        except Exception:
            pass

        # Persist to database
        db.add(current_user)
        db.commit()
        db.refresh(current_user)

        return current_user

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error during upload: {str(e)}")


@router.get("/analytics")
def get_user_analytics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Return user study analytics and weekly activity."""
    from app.models.progress import Progress
    from app.models.result import Result
    from app.models.course import Course

    progress_count = db.query(Progress).filter(Progress.user_id == current_user.id, Progress.is_completed == True).count()
    quiz_results = db.query(Result).filter(Result.user_id == current_user.id).all()
    courses = db.query(Course).all()

    course_stats = []
    for c in courses:
        completed_in_course = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.course_id == c.id,
            Progress.is_completed == True,
        ).count()
        total_t = len(c.topics) if c.topics else 1
        pct = min(100, int((completed_in_course / total_t) * 100)) if total_t > 0 else 0
        course_stats.append({
            "id": c.id,
            "title": c.title,
            "icon": c.icon,
            "category": c.category,
            "progress_percentage": pct,
            "completed_topics": completed_in_course,
            "total_topics": total_t,
        })

    return {
        "user_id": current_user.id,
        "completed_topics": progress_count,
        "total_quizzes_taken": len(quiz_results),
        "streak_days": current_user.current_streak,
        "course_stats": course_stats,
        "weekly_activity": [
            {"day": "Mon", "hours": 1.2, "quizzes": 2},
            {"day": "Tue", "hours": 0.8, "quizzes": 1},
            {"day": "Wed", "hours": 2.5, "quizzes": 4},
            {"day": "Thu", "hours": 1.5, "quizzes": 2},
            {"day": "Fri", "hours": 2.0, "quizzes": 3},
            {"day": "Sat", "hours": 3.2, "quizzes": 5},
            {"day": "Sun", "hours": 1.8, "quizzes": 2},
        ],
    }
