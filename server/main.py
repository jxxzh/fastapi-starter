import time
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from server.core.config import settings
from server.core.logger import logger
from server.routers import items


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


app.include_router(items.router)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the AI Herbal Formula System"}


def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
