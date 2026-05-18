from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class PredictionRequest(BaseModel):
    text: str
    mood_selection: Optional[str] = None

class PredictionResponse(BaseModel):
    prediction_id: str
    predicted_class: str
    confidence: float
    probabilities: dict
    recommendations: List[str]
    is_emergency: bool
    created_at: datetime

class PredictionInDB(BaseModel):
    id: str = Field(alias="_id")
    user_id: str
    input_text: str
    predicted_class: str
    confidence: float
    probabilities: dict
    is_emergency: bool
    created_at: datetime = Field(default_factory=datetime.utcnow)
