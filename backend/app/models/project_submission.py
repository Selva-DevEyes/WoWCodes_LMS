"""Project Submission model."""
from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base, TimestampMixin


class ProjectSubmission(Base, TimestampMixin):
    """Practical project submission for final evaluation certification."""

    __tablename__ = "project_submissions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False, index=True)
    project_title: Mapped[str] = mapped_column(String(200), nullable=False)
    github_url: Mapped[str] = mapped_column(String(500), nullable=False)
    live_demo_url: Mapped[str] = mapped_column(String(500), nullable=True)
    architecture_notes: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="evaluated", nullable=False)
    submitted_at = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User")
    course = relationship("Course")
