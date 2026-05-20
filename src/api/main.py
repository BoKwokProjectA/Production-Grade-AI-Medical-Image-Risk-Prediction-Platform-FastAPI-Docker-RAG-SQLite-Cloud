"""
Cloud Run entry point for the Copilot Studio support API.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.copilot_routes import copilot_router


app = FastAPI(
    title="ISIC Skin Lesion Platform Support API",
    version="1.0.0",
    description="Lightweight API used by the Copilot Studio support agent.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "status": "ok",
        "service": "ISIC Copilot Support API",
    }


@app.get("/api/v1/health")
async def health():
    return {
        "status": "ok",
        "service": "copilot-support-api",
    }


app.include_router(
    copilot_router,
    prefix="/api/v1",
    tags=["copilot-studio"],
)
