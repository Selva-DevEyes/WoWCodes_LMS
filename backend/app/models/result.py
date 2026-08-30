"""Result model - quiz attempt result."""
from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base, TimestampMixin


class Result(Base, TimestampMixin):
    """A user's quiz attempt result."""

    __tablename__ = "results"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    quiz_id: Mapped[int] = mapped_column(ForeignKey("quizzes.id"), nullable=False, index=True)
    score: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    total_points: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    percentage: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    passed: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    time_taken_seconds: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    rank: Mapped[str] = mapped_column(String(20), nullable=True)  # e.g. gold/silver/bronze

    user = relationship("User", back_populates="results")
    quiz = relationship("Quiz")
    answers = relationship("Answer", back_populates="result", cascade="all, delete-orphan")