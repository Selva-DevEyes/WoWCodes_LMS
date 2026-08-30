"""Result Pydantic schemas."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from app.schemas.common import ORMModel


class AnswerSubmit(BaseModel):
    """Answer submission payload."""

    question_id: int
    selected_option_id: int


class ResultSubmit(BaseModel):
    """Quiz result submission payload."""

    quiz_id: int
    time_taken_seconds: int = 0
    answers: List[AnswerSubmit] = Field(default_factory=list)


class AnswerResponse(ORMModel):
    """Answer response schema."""

    id: int
    question_id: int
    selected_option_id: int
    is_correct: int
    points_earned: int


class ResultResponse(ORMModel):
    """Result response schema."""

    id: int
    user_id: int
    quiz_id: int
    score: int
    total_points: int
    percentage: float
    passed: int
    time_taken_seconds: int
    rank: Optional[str] = None
    created_at: datetime
    answers: List[AnswerResponse] = Field(default_factory=list)