"""Role-based access control dependencies."""
from fastapi import Depends, HTTPException, status

from app.dependencies.auth import get_current_user
from app.models.user import User


def require_role(*allowed_roles: str):
    """Dependency factory returning a checked role dependency."""

    def role_checker(current_user: User = Depends(get_current_user)) -> User:
        role_name = current_user.role.name if current_user.role else ""
        if role_name not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action",
            )
        return current_user

    return role_checker


require_admin = require_role("admin")
require_instructor = require_role("admin", "instructor")
require_any = get_current_user
