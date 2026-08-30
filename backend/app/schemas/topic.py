"""Topic Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.common import ORMModel


class TopicBase(BaseModel):
    """Base topic fields."""

    course_id: int
    title: str = Field(min_length=3, max_length=200)
    slug: str = Field(min_length=3, max_length=200)
    description: Optional[str] = None
    content: Optional[str] = None
    order: int = 0
    estimated_minutes: int = 15


class TopicCreate(TopicBase):
    """Topic creation payload."""

    pass


class TopicUpdate(BaseModel):
    """Topic update payload."""

    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    order: Optional[int] = None
    estimated_minutes: Optional[int] = None


class TopicResponse(TopicBase, ORMModel):
    """Topic response schema."""

    id: int
    created_at: datetime
    updated_at: datetime