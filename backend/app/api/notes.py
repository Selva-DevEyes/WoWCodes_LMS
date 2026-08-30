"""Notes routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.note import Note
from app.models.user import User
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.get("", response_model=list[NoteResponse])
def my_notes(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Get the current user's notes."""
    return db.query(Note).filter(Note.user_id == current_user.id).order_by(Note.updated_at.desc()).all()


@router.post("", response_model=NoteResponse, status_code=201)
def create_note(
    payload: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Create a note for a topic."""
    note = Note(user_id=current_user.id, **payload.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.patch("/{note_id}", response_model=NoteResponse)
def update_note(
    note_id: int,
    payload: NoteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update a note."""
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user.id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(note, key, value)
    db.commit()
    db.refresh(note)
    return note


@router.delete("/{note_id}", status_code=204)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Delete a note."""
    note = db.query(Note).filter(Note.id == note_id, Note.user_id == current_user.id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
