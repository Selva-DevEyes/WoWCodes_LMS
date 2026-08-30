"""Bookmark Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.common import ORMModel


class BookmarkCreate(BaseModel):
    """Bookmark creation payload."""

    topic_id: Optional[int] = None
    lesson_id: Optional[int] = None
    title: str = Field(min_length=1, max_length=200)
    url: Optional[str] = None


class BookmarkResponse(ORMModel):
    """Bookmark response schema."""

    id: int
    user_id: int
    topic_id: Optional[int] = None
    lesson_id: Optional[int] = None
    title: str
    url: Optional[str] = None
    created_at: datetime