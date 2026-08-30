"""Bookmarks routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.bookmark import Bookmark
from app.models.user import User
from app.schemas.bookmark import BookmarkCreate, BookmarkResponse
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/bookmarks", tags=["Bookmarks"])


@router.get("", response_model=list[BookmarkResponse])
def my_bookmarks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Get the current user's bookmarks."""
    return db.query(Bookmark).filter(Bookmark.user_id == current_user.id).order_by(Bookmark.created_at.desc()).all()


@router.post("", response_model=BookmarkResponse, status_code=201)
def create_bookmark(
    payload: BookmarkCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a bookmark."""
    bookmark = Bookmark(user_id=current_user.id, **payload.model_dump())
    db.add(bookmark)
    db.commit()
    db.refresh(bookmark)
    return bookmark


@router.delete("/{bookmark_id}", status_code=204)
def delete_bookmark(
    bookmark_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete a bookmark."""
    bookmark = db.query(Bookmark).filter(
        Bookmark.id == bookmark_id,
        Bookmark.user_id == current_user.id,
    ).first()
    if bookmark is None:
        raise HTTPException(status_code=404, detail="Bookmark not found")
    db.delete(bookmark)
    db.commit()
