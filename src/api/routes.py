"""
API routes for skin lesion prediction.
"""

from datetime import datetime

from fastapi import APIRouter, UploadFile, File, HTTPException

from src.core.config import get_settings
from src.schemas.prediction import PredictionResponse, HealthResponse
from src.services.prediction_service import PredictionService


settings = get_settings()

health_router = APIRouter()
prediction_router = APIRouter()

prediction_service = PredictionService()


@health_router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        model_version=settings.MODEL_VERSION,
        api_version=settings.API_VERSION,
    )


@prediction_router.post(
    "/Predict",
    response_model=PredictionResponse,
    summary="Expand the block to predict skin lesion risk",
    description="""
Upload a skin lesion image and receive a malignant-risk prediction.

If the probability is in the review boundary range, the backend may trigger
a human-review workflow depending on the active PredictionService implementation.
""",
)
async def predict_image(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    result = await prediction_service.predict(file)

    probability = float(result["probability"])

    return PredictionResponse(
        isic_id=file.filename or "uploaded_image",
        probability=probability,
        prediction=result["prediction"],
        model_version=result.get("model_version", settings.MODEL_VERSION),
        timestamp=datetime.utcnow(),
        review_triggered=result.get(
            "review_triggered",
            0.45 <= probability <= 0.55,
        ),
    )
