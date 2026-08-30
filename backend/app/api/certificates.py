"""Certificates routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.certificate import Certificate
from app.models.user import User
from app.schemas.certificate import CertificateResponse
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/certificates", tags=["Certificates"])


@router.get("", response_model=list[CertificateResponse])
def my_certificates(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    """Get the current user's certificates."""
    return db.query(Certificate).filter(Certificate.user_id == current_user.id).all()


@router.get("/{certificate_code}", response_model=CertificateResponse)
def get_certificate(certificate_code: str, db: Session = Depends(get_db)):
    """Verify a certificate by code."""
    cert = db.query(Certificate).filter(Certificate.certificate_code == certificate_code).first()
    if cert is None:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return cert
