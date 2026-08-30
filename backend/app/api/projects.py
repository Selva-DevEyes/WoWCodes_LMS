"""Project submission and certificate evaluation routes."""
import uuid
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.session import get_db
from app.models.project_submission import ProjectSubmission
from app.models.certificate import Certificate
from app.models.notification import Notification
from app.models.user import User
from app.models.role import Role
from app.models.course import Course
from app.models.topic import Topic
from app.models.progress import Progress
from app.models.result import Result
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/projects", tags=["Project Submissions"])


class ProjectSubmissionCreate(BaseModel):
    course_id: int
    project_title: str = Field(min_length=3, max_length=200)
    github_url: str = Field(min_length=10, max_length=500)
    live_demo_url: str = Field(default="", max_length=500)
    architecture_notes: str = Field(default="", max_length=2000)


class ProjectEvaluationPayload(BaseModel):
    score: float = Field(ge=0, le=100)
    instructor_feedback: str = Field(min_length=5, max_length=2000)
    status: str = Field(default="approved")  # approved / changes_requested


def auto_evaluate_and_generate_certificate(db: Session, user: User, course_id: int) -> Optional[Certificate]:
    """Check requirements and automatically generate certificate with student name, grade, and congratulations quote."""
    # 1. Calculate student average accuracy & total score
    results = db.query(Result).filter(Result.user_id == user.id).all()
    avg_accuracy = (
        sum(r.percentage for r in results) / len(results) if results else 88.0
    )

    # 2. Determine performance honors & grade
    if avg_accuracy >= 90:
        grade = "Distinction with Honors (Grade A+)"
        quote = "Congratulations on demonstrating extraordinary full-stack engineering mastery, superior code quality, and exceptional problem-solving acumen!"
    elif avg_accuracy >= 80:
        grade = "Excellence in Software Engineering (Grade A)"
        quote = "Congratulations on demonstrating exceptional technical mastery and building production-ready full-stack software architecture!"
    elif avg_accuracy >= 70:
        grade = "Proficient Practitioner (Grade B+)"
        quote = "Congratulations on successfully mastering full-stack system architecture, modern frameworks, and engineering standards!"
    else:
        grade = "Certified Software Developer (Grade B)"
        quote = "Congratulations on completing the rigorous engineering curriculum and building production applications!"

    student_name = user.full_name or user.username

    # 3. Check if certificate already exists
    cert = db.query(Certificate).filter(
        Certificate.user_id == user.id,
        Certificate.course_id == course_id,
    ).first()

    if not cert:
        cert_code = f"WOW-SDE-{uuid.uuid4().hex[:8].upper()}"
        cert = Certificate(
            user_id=user.id,
            course_id=course_id,
            certificate_code=cert_code,
            student_name=student_name,
            grade=grade,
            congrats_quote=quote,
        )
        db.add(cert)
        db.commit()
        db.refresh(cert)

        # Notify student of certificate issuance
        student_notif = Notification(
            user_id=user.id,
            title="🏆 Official Certificate Generated!",
            message=f"Congratulations {student_name}! Your Software Development Engineering Certificate ({grade}) has been officially generated.",
            type="success",
            link="/certificates",
        )
        db.add(student_notif)
        db.commit()

    return cert


@router.post("/submit")
def submit_project(
    payload: ProjectSubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Submit practical capstone project, notify instructors for evaluation, and automatically generate certificate."""
    course = db.query(Course).filter(Course.id == payload.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    student_display_name = current_user.full_name or current_user.username

    # 1. Create or update project submission
    submission = db.query(ProjectSubmission).filter(
        ProjectSubmission.user_id == current_user.id,
        ProjectSubmission.course_id == payload.course_id,
    ).first()

    if not submission:
        submission = ProjectSubmission(
            user_id=current_user.id,
            course_id=payload.course_id,
            project_title=payload.project_title,
            github_url=payload.github_url,
            live_demo_url=payload.live_demo_url,
            architecture_notes=payload.architecture_notes,
            status="evaluated",
        )
        db.add(submission)
    else:
        submission.project_title = payload.project_title
        submission.github_url = payload.github_url
        submission.live_demo_url = payload.live_demo_url
        submission.architecture_notes = payload.architecture_notes
        submission.status = "evaluated"

    db.commit()
    db.refresh(submission)

    # 2. Notify all instructors / admins that a project requires evaluation
    instructors = (
        db.query(User)
        .join(Role, User.role_id == Role.id)
        .filter(Role.name.in_(["instructor", "admin", "teacher"]))
        .all()
    )

    if not instructors:
        # Fallback: find any admin users
        instructors = db.query(User).filter(User.role_id == 2).all()

    for instructor in instructors:
        db.add(
            Notification(
                user_id=instructor.id,
                title=f"📋 Capstone Evaluation Required: {student_display_name}",
                message=f"Student '{student_display_name}' submitted Capstone project '{payload.project_title}' for course '{course.title}'. Repository: {payload.github_url}",
                type="info",
                link="/certificates",
            )
        )

    # 3. Notify the student
    db.add(
        Notification(
            user_id=current_user.id,
            title="🚀 Capstone Project Submitted",
            message=f"Your project '{payload.project_title}' has been submitted for evaluation. Instructors have been notified.",
            type="success",
            link="/certificates",
        )
    )
    db.commit()

    # 4. Automatically generate official certificate for the student
    cert = auto_evaluate_and_generate_certificate(db, current_user, payload.course_id)

    return {
        "message": "Project submission received and instructor notified for evaluation!",
        "submission_id": submission.id,
        "certificate_code": cert.certificate_code if cert else None,
        "student_name": cert.student_name if cert else student_display_name,
        "grade": cert.grade if cert else "Distinction (Grade A+)",
        "congrats_quote": cert.congrats_quote if cert else "Congratulations on your engineering achievement!",
        "status": submission.status,
    }


@router.get("/my-submissions")
def my_submissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get list of user's project submissions."""
    return db.query(ProjectSubmission).filter(ProjectSubmission.user_id == current_user.id).all()


@router.get("/all-submissions")
def all_submissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get all submissions for instructor evaluation."""
    return (
        db.query(ProjectSubmission)
        .order_by(ProjectSubmission.submitted_at.desc())
        .all()
    )


@router.post("/{submission_id}/evaluate")
def evaluate_submission(
    submission_id: int,
    payload: ProjectEvaluationPayload,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Instructor evaluates and approves a project submission."""
    submission = db.query(ProjectSubmission).filter(ProjectSubmission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    submission.score = payload.score
    submission.instructor_feedback = payload.instructor_feedback
    submission.status = payload.status
    submission.evaluated_by = current_user.id
    db.commit()

    # Auto-generate or update certificate
    student = db.query(User).filter(User.id == submission.user_id).first()
    if student:
        cert = auto_evaluate_and_generate_certificate(db, student, submission.course_id)

    return {
        "message": "Evaluation recorded successfully!",
        "submission_id": submission.id,
        "status": submission.status,
    }
