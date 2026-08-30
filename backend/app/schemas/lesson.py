"""Lesson Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.common import ORMModel


class LessonBase(BaseModel):
    """Base lesson fields."""

    course_id: int
    topic_id: int
    title: str = Field(min_length=3, max_length=200)
    content: str
    order: int = 0


class LessonCreate(LessonBase):
    """Lesson creation payload."""

    pass


class LessonUpdate(BaseModel):
    """Lesson update payload."""

    title: Optional[str] = None
    content: Optional[str] = None
    order: Optional[int] = None
    is_published: Optional[bool] = None


class LessonResponse(LessonBase, ORMModel):
    """Lesson response schema."""

    id: int
    is_published: bool
    created_at: datetime
    updated_at: datetime