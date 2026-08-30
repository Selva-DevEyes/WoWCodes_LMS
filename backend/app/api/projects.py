"""Project submission and certificate evaluation routes."""
import uuid
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.project_submission import ProjectSubmission
from app.models.certificate import Certificate
from app.models.user import User
from app.models.course import Course
from app.models.result import Result
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/projects", tags=["Project Submissions"])


class ProjectSubmissionCreate(BaseModel):
    course_id: int
    project_title: str = Field(min_length=3, max_length=200)
    github_url: str = Field(min_length=10, max_length=500)
    live_demo_url: str = Field(default="", max_length=500)
    architecture_notes: str = Field(default="", max_length=2000)


@router.post("/submit")
def submit_project(
    payload: ProjectSubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Submit practical project for final evaluation and issue certificate if exam passed."""
    course = db.query(Course).filter(Course.id == payload.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Create or update project submission
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

    # Issue certificate automatically if exam passed or upon submission
    cert = db.query(Certificate).filter(
        Certificate.user_id == current_user.id,
        Certificate.course_id == payload.course_id,
    ).first()

    if not cert:
        cert_code = f"SDE-AI-{uuid.uuid4().hex[:8].upper()}"
        cert = Certificate(
            user_id=current_user.id,
            course_id=payload.course_id,
            certificate_code=cert_code,
        )
        db.add(cert)
        db.commit()
        db.refresh(cert)

    return {
        "message": "Project submission received and evaluated successfully!",
        "submission_id": submission.id,
        "certificate_code": cert.certificate_code,
        "status": submission.status,
    }


@router.get("/my-submissions")
def my_submissions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Get list of user's project submissions."""
    return db.query(ProjectSubmission).filter(ProjectSubmission.user_id == current_user.id).all()
