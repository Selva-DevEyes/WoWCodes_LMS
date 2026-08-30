"""User analytics and statistics API endpoints."""
from typing import Dict, Any, List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.models.progress import Progress
from app.models.result import Result
from app.models.course import Course
from app.models.topic import Topic
from app.models.quiz import Quiz

router = APIRouter(prefix="/users", tags=["Analytics"])


@router.get("/analytics")
def get_user_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Dict[str, Any]:
    """Retrieve detailed learning statistics and performance metrics for the current user."""
    # Completed topics count
    completed_topics_count = (
        db.query(Progress)
        .filter(Progress.user_id == current_user.id, Progress.is_completed == True)
        .count()
    )

    # Total topics count
    total_topics_count = db.query(Topic).count() or 1

    # Quiz results summary
    results = db.query(Result).filter(Result.user_id == current_user.id).all()
    quizzes_taken = len(results)
    avg_score = round(sum(r.percentage for r in results) / quizzes_taken, 1) if quizzes_taken > 0 else 0.0
    passed_quizzes = sum(1 for r in results if r.percentage >= 70.0)

    # Category breakdown (courses completed/in progress)
    courses = db.query(Course).all()
    course_stats = []
    for course in courses:
        course_topic_ids = [t.id for t in course.topics]
        if not course_topic_ids:
            continue
        completed_in_course = (
            db.query(Progress)
            .filter(
                Progress.user_id == current_user.id,
                Progress.topic_id.in_(course_topic_ids),
                Progress.is_completed == True,
            )
            .count()
        )
        pct = round((completed_in_course / len(course_topic_ids)) * 100, 1)
        course_stats.append({
            "id": course.id,
            "title": course.title,
            "category": course.category,
            "icon": course.icon,
            "total_topics": len(course_topic_ids),
            "completed_topics": completed_in_course,
            "progress_percentage": pct,
        })

    # Weekly activity mock/derived data (Mon-Sun)
    weekly_activity = [
        {"day": "Mon", "hours": 1.2, "quizzes": 2},
        {"day": "Tue", "hours": 0.8, "quizzes": 1},
        {"day": "Wed", "hours": 2.5, "quizzes": 4},
        {"day": "Thu", "hours": 1.5, "quizzes": 2},
        {"day": "Fri", "hours": 2.0, "quizzes": 3},
        {"day": "Sat", "hours": 3.0, "quizzes": 5},
        {"day": "Sun", "hours": 1.8, "quizzes": 2},
    ]

    return {
        "user_id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "learning_score": current_user.total_score or 0,
        "current_streak_days": current_user.current_streak or 1,
        "total_topics_count": total_topics_count,
        "completed_topics_count": completed_topics_count,
        "overall_progress_pct": round((completed_topics_count / total_topics_count) * 100, 1),
        "quizzes_taken": quizzes_taken,
        "quiz_avg_accuracy_pct": avg_score,
        "quizzes_passed": passed_quizzes,
        "course_stats": course_stats,
        "weekly_activity": weekly_activity,
    }
