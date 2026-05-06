"""
Database models for storing prediction records
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PredictionRecord(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    isic_id = Column(String, index=True)
    probability = Column(Float)
    prediction = Column(String)
    model_version = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    image_filename = Column(String, nullable=True)
    user_feedback = Column(String, nullable=True)

