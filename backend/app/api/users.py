"""User routes."""
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, Depends, File, HTTPException, Request, UploadFile, status
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
    """Upload and assign a profile image for the current user."""
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

        # Create directory and save file
        avatar_dir = Path(__file__).resolve().parents[2] / "uploads" / "avatars"
        try:
            avatar_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to create upload directory: {str(e)}")

        # Generate unique filename
        filename = f"user-{current_user.id}-{uuid4().hex}{extension}"
        filepath = avatar_dir / filename

        # Write file with error handling
        try:
            filepath.write_bytes(content)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to save image: {str(e)}")

        # Build avatar URL - using request base URL
        avatar_path = f"/uploads/avatars/{filename}"
        base_url = str(request.base_url).rstrip('/')
        current_user.avatar_url = f"{base_url}{avatar_path}"

        # Persist to database
        try:
            db.add(current_user)
            db.commit()
            db.refresh(current_user)
        except Exception as e:
            db.rollback()
            # Try to delete the file if database commit failed
            try:
                filepath.unlink()
            except:
                pass
            raise HTTPException(status_code=500, detail=f"Failed to save to database: {str(e)}")

        return current_user

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Unexpected error during upload: {str(e)}")


@router.get("/leaderboard")
def get_leaderboard(db: Session = Depends(get_db), limit: int = 10):
    """Return top users by score."""
    users = db.query(User).order_by(User.total_score.desc()).limit(limit).all()
    return [
        {
            "rank": idx + 1,
            "user_id": u.id,
            "username": u.username,
            "full_name": u.full_name,
            "total_score": u.total_score,
            "current_streak": u.current_streak,
            "avatar_url": u.avatar_url,
        }
        for idx, u in enumerate(users)
    ]
