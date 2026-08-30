"""Certificate Pydantic schemas."""
from datetime import datetime
from typing import Optional
from app.schemas.common import ORMModel


class CertificateResponse(ORMModel):
    """Certificate response schema."""

    id: int
    user_id: int
    course_id: int
    certificate_code: str
    student_name: Optional[str] = None
    grade: Optional[str] = "Distinction (Grade A+)"
    congrats_quote: Optional[str] = "Congratulations on demonstrating exceptional technical mastery and building production-ready full-stack software architecture!"
    issued_at: datetime
