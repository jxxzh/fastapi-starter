import time
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from server.core.config import settings
from server.core.logger import logger
from server.routers import health, items


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Actions on startup
    logger.info(f"Starting up app: {settings.APP_NAME}")
    logger.info("Loading resources...")
    yield
    # Actions on shutdown
    logger.info("Shutting down...")
    logger.info("Releasing resources...")


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)


# Global exception handler for HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(
        f"HTTP exception: {exc.detail} - {request.method} {request.url.path}"
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "status_code": exc.status_code},
    )


# Global exception handler for unexpected errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)} - {request.method} {request.url.path}")
    return JSONResponse(
        status_code=500, content={"error": "Internal server error", "status_code": 500}
    )


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(
        f"'{request.method} {request.url.path}' "
        f"{response.status_code} {process_time:.4f}s"
    )
    return response


# Include routers
app.include_router(items.router)
app.include_router(health.router)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the FastAPI Starter"}


def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
