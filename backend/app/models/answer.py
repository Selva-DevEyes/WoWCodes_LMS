"""Answer model - user's answer to a question."""
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base, TimestampMixin


class Answer(Base, TimestampMixin):
    """User's answer to a quiz question."""

    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    result_id: Mapped[int] = mapped_column(ForeignKey("results.id"), nullable=False, index=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("questions.id"), nullable=False, index=True)
    selected_option_id: Mapped[int] = mapped_column(ForeignKey("options.id"), nullable=False)
    is_correct: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    points_earned: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    result = relationship("Result", back_populates="answers")
    question = relationship("Question", back_populates="answers")
    selected_option = relationship("Option", foreign_keys=[selected_option_id])