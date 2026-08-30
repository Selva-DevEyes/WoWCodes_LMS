"""Auth-related Pydantic schemas."""
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    """User registration payload."""

    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    full_name: Optional[str] = Field(default=None, max_length=255)
    password: str = Field(min_length=8, max_length=128)


class LoginRequest(BaseModel):
    """User login payload."""

    email: EmailStr
    password: str


class ForgotPasswordRequest(BaseModel):
    """Forgot password payload."""

    email: EmailStr


class ResetPasswordRequest(BaseModel):
    """Reset password payload."""

    token: str
    new_password: str = Field(min_length=8, max_length=128)


class RefreshTokenRequest(BaseModel):
    """Refresh token payload."""

    refresh_token: str