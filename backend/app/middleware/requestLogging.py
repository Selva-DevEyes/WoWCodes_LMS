"""Request logging middleware."""
import time
import logging

logger = logging.getLogger("uvicorn.access")


async def log_requests(request, call_next):
    """Log request method, path, and duration."""
    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000
    logger.info(f"{request.method} {request.url.path} - {response.status_code} - {duration:.0f}ms")
    return response
