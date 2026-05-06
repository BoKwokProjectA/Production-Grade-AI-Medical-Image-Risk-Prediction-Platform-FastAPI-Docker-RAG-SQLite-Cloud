"""
Repository layer for prediction records
"""

from sqlalchemy.orm import Session
from src.db.models import PredictionRecord
from datetime import datetime

class PredictionRepository:
    def __init__(self, db: Session):
        self.db = db

    def save_prediction(self, isic_id: str, probability: float, prediction: str,
                       model_version: str, image_filename: str = None):
        record = PredictionRecord(
            isic_id=isic_id,
            probability=probability,
            prediction=prediction,
            model_version=model_version,
            timestamp=datetime.utcnow(),
            image_filename=image_filename
        )
        self.db.add(record)
        self.db.commit()
        self.db.refresh(record)
        return record

