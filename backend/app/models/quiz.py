"""Quiz model."""
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base, TimestampMixin


class Quiz(Base, TimestampMixin):
    """Quiz for a topic (Easy/Medium/Hard)."""

    __tablename__ = "quizzes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    level: Mapped[str] = mapped_column(String(20), nullable=False, index=True)  # easy/moderate/hard
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    time_limit_minutes: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
    passing_score: Mapped[int] = mapped_column(Integer, default=60, nullable=False)

    topic = relationship("Topic", back_populates="quizzes")
    questions = relationship("Question", back_populates="quiz", cascade="all, delete-orphan")