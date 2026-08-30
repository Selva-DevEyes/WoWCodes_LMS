"""Quiz and result routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.quiz import Quiz
from app.models.question import Question
from app.models.option import Option
from app.models.result import Result
from app.models.answer import Answer
from app.models.user import User
from app.models.progress import Progress
from app.models.notification import Notification
from app.schemas.quiz import QuizResponse, QuizDetailResponse
from app.schemas.result import ResultSubmit, ResultResponse
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/quiz", tags=["Quiz"])


@router.get("/topic/{topic_id}", response_model=list[QuizResponse])
def list_quizzes(topic_id: int, db: Session = Depends(get_db)):
    """List quizzes for a topic."""
    return db.query(Quiz).filter(Quiz.topic_id == topic_id).all()


@router.get("/{quiz_id}", response_model=QuizDetailResponse)
def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    """Get quiz detail with questions and options."""
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz


@router.post("/{quiz_id}/submit", response_model=ResultResponse)
def submit_quiz(
    quiz_id: int,
    payload: ResultSubmit,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Submit quiz answers and get a result."""
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")

    score = 0
    total_points = 0
    answer_models = []

    for question in quiz.questions:
        total_points += question.points
        correct_option = next((o for o in question.options if o.is_correct), None)
        submitted = next((a for a in payload.answers if a.question_id == question.id), None)
        is_correct = 0
        points_earned = 0
        selected_option_id = submitted.selected_option_id if submitted else None

        if correct_option and submitted and submitted.selected_option_id == correct_option.id:
            is_correct = 1
            points_earned = question.points
            score += question.points

        answer_models.append(
            Answer(
                question_id=question.id,
                selected_option_id=selected_option_id,
                is_correct=is_correct,
                points_earned=points_earned,
            )
        )

    percentage = round((score / total_points * 100), 2) if total_points else 0.0
    passed = 1 if percentage >= quiz.passing_score else 0

    result = Result(
        user_id=current_user.id,
        quiz_id=quiz.id,
        score=score,
        total_points=total_points,
        percentage=percentage,
        passed=passed,
        time_taken_seconds=payload.time_taken_seconds,
        rank=("gold" if percentage >= 90 else "silver" if percentage >= 70 else "bronze" if passed else None),
    )
    for a in answer_models:
        a.result = result
    db.add(result)

    # Update progress
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.topic_id == quiz.topic_id,
    ).first()
    if progress is None:
        progress = Progress(
            user_id=current_user.id,
            topic_id=quiz.topic_id,
            course_id=quiz.topic.course_id,
            quiz_completed=passed == 1,
        )
        db.add(progress)
    else:
        progress.quiz_completed = progress.quiz_completed or (passed == 1)

    # Update user score
    current_user.total_score += score

    # Notification
    db.add(Notification(
        user_id=current_user.id,
        title="Quiz Completed",
        message=f"You scored {percentage}% on {quiz.title}",
        type="success" if passed else "info",
        link=f"/quiz/{quiz.id}/result/{result.id}",
    ))

    db.commit()
    db.refresh(result)
    return result


@router.get("/results/mine", response_model=list[ResultResponse])
def my_results(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Get the current user's quiz results."""
    return db.query(Result).filter(Result.user_id == current_user.id).order_by(Result.created_at.desc()).all()
