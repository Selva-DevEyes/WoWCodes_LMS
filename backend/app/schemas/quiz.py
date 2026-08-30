"""Quiz Pydantic schemas."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.schemas.common import ORMModel


class OptionInput(BaseModel):
    """Quiz option creation schema."""

    text: str
    is_correct: bool = False
    order: int = 0


class QuestionInput(BaseModel):
    """Quiz question creation schema."""

    text: str
    explanation: Optional[str] = None
    points: int = 10
    order: int = 0
    options: List[OptionInput] = Field(default_factory=list)


class OptionResponse(ORMModel):
    """Quiz option response schema."""

    id: int
    text: str
    is_correct: bool
    order: int


class QuestionResponse(ORMModel):
    """Quiz question response schema."""

    id: int
    text: str
    explanation: Optional[str] = None
    points: int
    order: int
    options: List[OptionResponse] = Field(default_factory=list)


class QuizBase(BaseModel):
    """Base quiz fields."""

    topic_id: int
    title: str = Field(min_length=3, max_length=200)
    level: str = "easy"  # easy / moderate / hard
    description: Optional[str] = None
    time_limit_minutes: int = 10
    passing_score: int = 60


class QuizCreate(QuizBase):
    """Quiz creation payload."""

    questions: List[QuestionInput] = Field(default_factory=list)


class QuizUpdate(BaseModel):
    """Quiz update payload."""

    title: Optional[str] = None
    level: Optional[str] = None
    description: Optional[str] = None
    time_limit_minutes: Optional[int] = None
    passing_score: Optional[int] = None


class QuizResponse(QuizBase, ORMModel):
    """Quiz response schema."""

    id: int
    created_at: datetime
    updated_at: datetime


class QuizDetailResponse(QuizResponse):
    """Quiz detail with questions."""

    questions: List[QuestionResponse] = Field(default_factory=list)