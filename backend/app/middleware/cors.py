"""CORS middleware configuration."""
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings


def setup_cors(app):
    """Add CORS middleware to the app."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
