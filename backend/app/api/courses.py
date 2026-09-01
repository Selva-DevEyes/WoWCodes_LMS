"""Course routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseUpdate, CourseResponse
from app.dependencies.roles import require_admin, require_instructor
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/seed-now")
@router.post("/seed-now")
def seed_database_endpoint():
    """Seed all 14 learning paths, topics, and quizzes into the database."""
    from app.seed.seed_all_14_paths import seed_database
    seed_database()
    return {"message": "Curriculum database seeded successfully with all 14 courses, modules, topics, and quizzes!"}


@router.get("", response_model=list[CourseResponse])
def list_courses(db: Session = Depends(get_db)):
    """List published courses."""
    return db.query(Course).filter(Course.is_published.is_(True)).order_by(Course.order).all()


@router.get("/all", response_model=list[CourseResponse])
def list_all_courses(db: Session = Depends(get_db), _: User = Depends(require_instructor)):
    """List all courses (instructor/admin only)."""
    return db.query(Course).order_by(Course.order).all()


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    """Get a single course."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.post("", response_model=CourseResponse, status_code=201)
def create_course(
    payload: CourseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_instructor),
):
    """Create a new course (instructor/admin only)."""
    if db.query(Course).filter(Course.slug == payload.slug).first():
        raise HTTPException(status_code=400, detail="Course slug already exists")
    course = Course(**payload.model_dump(), instructor_id=current_user.id)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


@router.patch("/{course_id}", response_model=CourseResponse)
def update_course(
    course_id: int,
    payload: CourseUpdate,
    db: Session = Depends(get_db),
    _: User = Depends(require_instructor),
):
    """Update a course (instructor/admin only)."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(course, key, value)
    db.commit()
    db.refresh(course)
    return course


@router.delete("/{course_id}", status_code=204)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(require_admin),
):
    """Delete a course (admin only)."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
