from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from server.core.config import settings
from server.core.handlers import api_exception_handler, general_exception_handler
from server.core.logger import logger
from server.core.middlewares import LoggingMiddleware, RequestIDMiddleware
from server.routers import health, items
from server.schemas.api import APIError


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Actions on startup
    logger.info(f"Starting up app: {settings.APP_NAME}")
    logger.info("Loading resources...")
    yield
    # Actions on shutdown
    logger.info("Shutting down...")
    logger.info("Releasing resources...")


app = FastAPI(
    lifespan=lifespan,
)

# 添加中间件 - 注意顺序很重要！
# RequestIDMiddleware 必须在 LoggingMiddleware 之前，因为日志需要 request_id
app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)

# 添加异常处理器
app.add_exception_handler(APIError, api_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)


# 添加路由
app.include_router(health.router, tags=["Health"], prefix="/health")
app.include_router(items.router, tags=["Items"], prefix="/items")


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the FastAPI Starter"}


def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
