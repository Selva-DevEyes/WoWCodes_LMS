"""Note model."""
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base, TimestampMixin


class Note(Base, TimestampMixin):
    """User notes for a topic."""

    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False, index=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False, default="Untitled Note")
    content: Mapped[str] = mapped_column(Text, nullable=False)

    user = relationship("User", back_populates="notes")
    topic = relationship("Topic", back_populates="notes")