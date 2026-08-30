"""Core security helpers."""
import secrets
from datetime import datetime, timedelta, timezone
from typing import Optional


def generate_password_reset_token() -> str:
    """Generate a cryptographically secure random token."""
    return secrets.token_urlsafe(32)


def is_token_expired(token_created_at: Optional[datetime], expires_minutes: int) -> bool:
    """Check if a token created at token_created_at is expired."""
    if token_created_at is None:
        return True
    now = datetime.now(timezone.utc)
    if token_created_at.tzinfo is None:
        token_created_at = token_created_at.replace(tzinfo=timezone.utc)
    return now - token_created_at > timedelta(minutes=expires_minutes)


__all__ = ["generate_password_reset_token", "is_token_expired"]