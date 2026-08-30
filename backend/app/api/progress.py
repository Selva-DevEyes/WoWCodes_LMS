"""Progress and dashboard routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.progress import Progress
from app.models.user import User
from app.models.topic import Topic
from app.models.course import Course
from app.models.certificate import Certificate
from app.models.result import Result
from app.schemas.progress import ProgressUpdate, ProgressResponse, DashboardStats
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/progress", tags=["Progress"])


@router.get("/dashboard", response_model=DashboardStats)
def dashboard_stats(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Get user's dashboard statistics."""
    total_topics = db.query(Topic).count()
    completed = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.is_completed.is_(True),
    ).count()
    quiz_done = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.quiz_completed.is_(True),
    ).count()
    projects_done = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.project_completed.is_(True),
    ).count()
    certs = db.query(Certificate).filter(Certificate.user_id == current_user.id).count()

    return DashboardStats(
        total_courses=db.query(Course).count(),
        total_topics=total_topics,
        completed_topics=completed,
        quiz_completed=quiz_done,
        projects_completed=projects_done,
        learning_percentage=round((completed / total_topics * 100), 1) if total_topics else 0,
        current_streak=current_user.current_streak,
        total_score=current_user.total_score,
        certificates_count=certs,
    )


@router.get("", response_model=list[ProgressResponse])
def my_progress(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Get the current user's learning progress."""
    return db.query(Progress).filter(Progress.user_id == current_user.id).all()


@router.get("/topic/{topic_id}", response_model=ProgressResponse)
def get_topic_progress(
    topic_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get progress for a specific topic."""
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.topic_id == topic_id,
    ).first()
    if progress is None:
        raise HTTPException(status_code=404, detail="No progress found for this topic")
    return progress


@router.post("/topic/{topic_id}", response_model=ProgressResponse)
def upsert_progress(
    topic_id: int,
    payload: ProgressUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create or update progress for a topic."""
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.topic_id == topic_id,
    ).first()

    if progress is None:
        topic = db.query(Topic).filter(Topic.id == topic_id).first()
        if topic is None:
            raise HTTPException(status_code=404, detail="Topic not found")
        progress = Progress(
            user_id=current_user.id,
            topic_id=topic_id,
            course_id=topic.course_id,
        )
        db.add(progress)

    if payload.is_completed is not None:
        progress.is_completed = payload.is_completed
        if payload.is_completed and not progress.completed_at:
            from datetime import datetime
            progress.completed_at = datetime.now()
    if payload.quiz_completed is not None:
        progress.quiz_completed = payload.quiz_completed
    if payload.project_completed is not None:
        progress.project_completed = payload.project_completed
    if payload.last_position_seconds is not None:
        progress.last_position_seconds = payload.last_position_seconds

    db.commit()
    db.refresh(progress)
    return progress
