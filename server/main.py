from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from server.core.config import settings
from server.routers import items


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Actions on startup
    print(f"Starting up app: {settings.APP_NAME}")
    print("Loading resources...")
    yield
    # Actions on shutdown
    print("Shutting down...")
    print("Releasing resources...")


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.include_router(items.router)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the AI Herbal Formula System"}


def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
