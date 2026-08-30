"""Search routes."""
from fastapi import APIRouter, Depends, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.topic import Topic
from app.models.course import Course
from app.models.quiz import Quiz
from app.models.note import Note
from app.schemas.search import SearchResult

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("", response_model=list[SearchResult])
def global_search(
    q: str = Query(..., min_length=1, max_length=100),
    db: Session = Depends(get_db),
):
    """Search across topics, notes, quizzes, and courses."""
    query = f"%{q}%"
    results = []

    # Search topics
    for topic in db.query(Topic).filter(
        or_(Topic.title.ilike(query), Topic.description.ilike(query))
    ).all():
        results.append(SearchResult(
            type="topic",
            id=topic.id,
            title=topic.title,
            description=topic.description,
            url=f"/learn/topic/{topic.id}",
        ))

    # Search courses
    for course in db.query(Course).filter(
        or_(Course.title.ilike(query), Course.description.ilike(query))
    ).all():
        results.append(SearchResult(
            type="course",
            id=course.id,
            title=course.title,
            description=course.description,
            url=f"/learn/course/{course.id}",
        ))

    # Search quizzes
    for quiz in db.query(Quiz).filter(Quiz.title.ilike(query)).all():
        results.append(SearchResult(
            type="quiz",
            id=quiz.id,
            title=quiz.title,
            url=f"/quiz/{quiz.id}",
        ))

    return results[:20]
