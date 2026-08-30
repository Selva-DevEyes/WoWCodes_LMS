"""Progress Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.schemas.common import ORMModel


class ProgressUpdate(BaseModel):
    """Progress update payload."""

    is_completed: Optional[bool] = None
    quiz_completed: Optional[bool] = None
    project_completed: Optional[bool] = None
    last_position_seconds: Optional[int] = None


class ProgressResponse(ORMModel):
    """Progress response schema."""

    id: int
    user_id: int
    topic_id: int
    course_id: int
    is_completed: bool
    quiz_completed: bool
    project_completed: bool
    last_position_seconds: int
    completed_at: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime


class DashboardStats(BaseModel):
    """Dashboard statistics response."""

    total_courses: int = 0
    total_topics: int = 0
    completed_topics: int = 0
    quiz_completed: int = 0
    projects_completed: int = 0
    learning_percentage: float = 0.0
    current_streak: int = 0
    total_score: int = 0
    certificates_count: int = 0