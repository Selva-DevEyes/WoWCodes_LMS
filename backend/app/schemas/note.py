"""Note Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.common import ORMModel


class NoteBase(BaseModel):
    """Base note fields."""

    topic_id: int
    title: str = Field(default="Untitled Note", max_length=200)
    content: str


class NoteCreate(NoteBase):
    """Note creation payload."""

    pass


class NoteUpdate(BaseModel):
    """Note update payload."""

    title: Optional[str] = None
    content: Optional[str] = None


class NoteResponse(NoteBase, ORMModel):
    """Note response schema."""

    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime