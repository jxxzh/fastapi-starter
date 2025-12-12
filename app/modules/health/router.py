from app.core.logger import logger
from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get("/")
async def health_check():
    """Health check endpoint."""
    logger.info("Health check requested")
    return {"status": "healthy", "service": "FastAPI Starter", "version": "1.0.0"}
