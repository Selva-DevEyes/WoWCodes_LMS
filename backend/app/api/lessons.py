"""Lessons routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.lesson import Lesson
from app.schemas.lesson import LessonResponse
from app.dependencies.roles import require_instructor

router = APIRouter(prefix="/lessons", tags=["Lessons"])


@router.get("/topic/{topic_id}", response_model=list[LessonResponse])
def list_lessons(topic_id: int, db: Session = Depends(get_db)):
    """List lessons for a topic."""
    return db.query(Lesson).filter(Lesson.topic_id == topic_id).order_by(Lesson.order).all()


@router.get("/{lesson_id}", response_model=LessonResponse)
def get_lesson(lesson_id: int, db: Session = Depends(get_db)):
    """Get a single lesson."""
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson
