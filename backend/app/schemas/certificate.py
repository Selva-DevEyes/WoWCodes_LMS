"""Certificate Pydantic schemas."""
from datetime import datetime
from pydantic import BaseModel
from app.schemas.common import ORMModel


class CertificateResponse(ORMModel):
    """Certificate response schema."""

    id: int
    user_id: int
    course_id: int
    certificate_code: str
    issued_at: datetime
