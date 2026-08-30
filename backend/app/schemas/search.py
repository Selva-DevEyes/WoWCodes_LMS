"""Search and leaderboard Pydantic schemas."""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.schemas.common import ORMModel


class SearchResult(BaseModel):
    """Search result item."""

    type: str  # topic / note / quiz / interview-question / project
    id: int
    title: str
    description: Optional[str] = None
    url: str
    score: float = 0.0


class LeaderboardEntry(BaseModel):
    """Leaderboard entry."""

    rank: int
    user_id: int
    username: str
    full_name: Optional[str] = None
    total_score: int
    current_streak: int
    avatar_url: Optional[str] = None
