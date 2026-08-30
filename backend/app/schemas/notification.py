"""Notification Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.schemas.common import ORMModel


class NotificationCreate(BaseModel):
    """Notification creation payload."""

    user_id: int
    title: str = Field(min_length=1, max_length=200)
    message: str
    type: str = "info"
    link: Optional[str] = None


class NotificationResponse(ORMModel):
    """Notification response schema."""

    id: int
    user_id: int
    title: str
    message: str
    type: str
    is_read: bool
    link: Optional[str] = None
    created_at: datetime
