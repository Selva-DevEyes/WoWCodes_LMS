"""User Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.schemas.common import ORMModel


class UserResponse(ORMModel):
    """User response schema."""

    id: int
    email: EmailStr
    username: str
    full_name: Optional[str] = None
    role_id: int
    is_active: bool
    is_verified: bool
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    total_score: int = 0
    current_streak: int = 0
    created_at: datetime


class UserUpdate(BaseModel):
    """User update payload."""

    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None