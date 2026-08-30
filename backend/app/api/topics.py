"""Topic routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.topic import Topic
from app.schemas.topic import TopicCreate, TopicUpdate, TopicResponse
from app.dependencies.roles import require_instructor

router = APIRouter(prefix="/topics", tags=["Topics"])


@router.get("/course/{course_id}", response_model=list[TopicResponse])
def list_topics(course_id: int, db: Session = Depends(get_db)):
    """List topics for a course."""
    return db.query(Topic).filter(Topic.course_id == course_id).order_by(Topic.order).all()


@router.get("/{topic_id}", response_model=TopicResponse)
def get_topic(topic_id: int, db: Session = Depends(get_db)):
    """Get a single topic."""
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    return topic


@router.post("", response_model=TopicResponse, status_code=201)
def create_topic(payload: TopicCreate, db: Session = Depends(get_db), _=Depends(require_instructor)):
    """Create a new topic (instructor only)."""
    if db.query(Topic).filter(Topic.slug == payload.slug).first():
        raise HTTPException(status_code=400, detail="Topic slug already exists")
    topic = Topic(**payload.model_dump())
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic


@router.patch("/{topic_id}", response_model=TopicResponse)
def update_topic(
    topic_id: int,
    payload: TopicUpdate,
    db: Session = Depends(get_db),
    _=Depends(require_instructor),
):
    """Update a topic (instructor only)."""
    topic = db.query(Topic).filter(Topic.id == topic_id).first()
    if topic is None:
        raise HTTPException(status_code=404, detail="Topic not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(topic, key, value)
    db.commit()
    db.refresh(topic)
    return topic
