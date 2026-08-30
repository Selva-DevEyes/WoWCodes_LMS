"""Database session management with PostgreSQL support for Render deployment."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool

from app.core.config import settings

# Handle Render PostgreSQL URL prefix (postgres:// -> postgresql://)
db_url = os.getenv("DATABASE_URL", settings.DATABASE_URL)
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql://", 1)

# Detect SQLite vs PostgreSQL / MySQL
if db_url.startswith("sqlite"):
    engine = create_engine(
        db_url,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    engine = create_engine(
        db_url,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20,
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """FastAPI dependency that yields a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db() -> None:
    """Initialize database tables and auto-seed initial curriculum data if empty."""
    from app.models import (  # noqa: F401
        role,
        user,
        course,
        topic,
        lesson,
        note,
        quiz,
        question,
        option,
        answer,
        result,
        progress,
        bookmark,
        certificate,
        notification,
    )
    from app.database.base import Base

    Base.metadata.create_all(bind=engine)

    # Auto-seed if database tables are empty (e.g. fresh Render PostgreSQL deployment)
    db = SessionLocal()
    try:
        from app.models.course import Course
        if db.query(Course).count() == 0:
            print("Fresh database detected! Running initial curriculum seeder...")
            try:
                from scratch.seed_all_14_paths import seed_curriculum
                seed_curriculum()
            except ImportError:
                pass
    except Exception as e:
        print(f"Auto-seed check note: {e}")
    finally:
        db.close()