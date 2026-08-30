"""Course Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.common import ORMModel


class CourseBase(BaseModel):
    """Base course fields."""

    title: str = Field(min_length=3, max_length=200)
    slug: str = Field(min_length=3, max_length=200)
    description: Optional[str] = None
    category: str = Field(min_length=2, max_length=100)
    level: str = "beginner"
    icon: Optional[str] = None
    color: Optional[str] = None
    order: int = 0


class CourseCreate(CourseBase):
    """Course creation payload."""

    pass


class CourseUpdate(BaseModel):
    """Course update payload."""

    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    level: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    is_published: Optional[bool] = None
    order: Optional[int] = None


class CourseResponse(CourseBase, ORMModel):
    """Course response schema."""

    id: int
    instructor_id: Optional[int] = None
    is_published: bool
    created_at: datetime
    updated_at: datetime