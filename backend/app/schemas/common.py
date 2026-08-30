"""Common Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ORMModel(BaseModel):
    """Base schema with ORM mode enabled."""

    model_config = ConfigDict(from_attributes=True)


class MessageResponse(BaseModel):
    """Simple message response."""

    message: str


class TokenResponse(BaseModel):
    """JWT token response."""

    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"


class PaginatedResponse(BaseModel):
    """Generic paginated response."""

    total: int
    page: int
    page_size: int
    items: list