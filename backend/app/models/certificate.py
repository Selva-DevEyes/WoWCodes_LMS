"""Certificate model."""
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base, TimestampMixin


class Certificate(Base, TimestampMixin):
    """Certificate awarded to a user for completing a course."""

    __tablename__ = "certificates"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    certificate_code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    student_name: Mapped[str] = mapped_column(String(255), nullable=True)
    grade: Mapped[str] = mapped_column(String(100), default="Distinction (Grade A+)", nullable=True)
    congrats_quote: Mapped[str] = mapped_column(
        String(500),
        default="Congratulations on demonstrating exceptional technical mastery and building production-ready full-stack software architecture!",
        nullable=True,
    )
    issued_at = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="certificates")
    course = relationship("Course")