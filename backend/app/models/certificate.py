"""Certificate model."""
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base, TimestampMixin


class Certificate(Base, TimestampMixin):
    """Certificate awarded to a user for completing a course."""

    __tablename__ = "certificates"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    certificate_code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    issued_at = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="certificates")
    course = relationship("Course")