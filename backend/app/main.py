"""WoWCodes API entry point."""
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import settings
from app.database.session import init_db
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.courses import router as courses_router
from app.api.topics import router as topics_router
from app.api.lessons import router as lessons_router
from app.api.notes import router as notes_router
from app.api.quiz import router as quiz_router
from app.api.progress import router as progress_router
from app.api.bookmarks import router as bookmarks_router
from app.api.notifications import router as notifications_router
from app.api.certificates import router as certificates_router
from app.api.search import router as search_router
from app.api.playground import router as playground_router
from app.api.analytics import router as analytics_router
from app.api.projects import router as projects_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database tables on startup."""
    init_db()
    yield


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="WoWCodes LMS API - Learn Practice Build Crack Interviews",
    lifespan=lifespan,
)

# Locally uploaded profile images are served from this directory.
uploads_dir = Path(__file__).resolve().parents[1] / "uploads"
uploads_dir.mkdir(parents=True, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=uploads_dir), name="uploads")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Router
api_prefix = "/api/v1"
app.include_router(auth_router, prefix=api_prefix)
app.include_router(users_router, prefix=api_prefix)
app.include_router(courses_router, prefix=api_prefix)
app.include_router(topics_router, prefix=api_prefix)
app.include_router(lessons_router, prefix=api_prefix)
app.include_router(notes_router, prefix=api_prefix)
app.include_router(quiz_router, prefix=api_prefix)
app.include_router(progress_router, prefix=api_prefix)
app.include_router(bookmarks_router, prefix=api_prefix)
app.include_router(notifications_router, prefix=api_prefix)
app.include_router(certificates_router, prefix=api_prefix)
app.include_router(search_router, prefix=api_prefix)
app.include_router(playground_router, prefix=api_prefix)
app.include_router(analytics_router, prefix=api_prefix)
app.include_router(projects_router, prefix=api_prefix)


@app.get("/")
def root():
    """Root endpoint."""
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
