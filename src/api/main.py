"""
Main FastAPI application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.core.config import get_settings
from src.core.logger import logger
from src.api.routes import health_router, prediction_router
from src.api.rag_routes import rag_router

settings = get_settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application starting up", app_name=settings.APP_NAME)
    yield
    logger.info("Application shutting down")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION,
    description="ISIC 2024 Skin Cancer Detection API",
    lifespan=lifespan
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

app.include_router(health_router, prefix="/api/v1", tags=["health"])
app.include_router(prediction_router, prefix="/api/v1", tags=["prediction"])
app.include_router(rag_router, prefix="/api/v1", tags=["rag"])

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "ISIC 2024 Flagship API is running"}

