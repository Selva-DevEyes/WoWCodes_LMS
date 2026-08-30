"""Error handler middleware."""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def setup_error_handlers(app: FastAPI):
    """Register global exception handlers."""

    @app.exception_handler(Exception)
    async def unhandled_exception(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"detail": "An unexpected error occurred"},
        )
