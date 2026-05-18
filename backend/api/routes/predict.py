from fastapi import APIRouter, Depends
from typing import Annotated
from ...models.user import UserInDB
from ...models.prediction import PredictionRequest, PredictionResponse
from ...services.model_service import predictor
from ...services.recommendation_service import get_recommendations
from .auth import get_current_user
from ...database import get_database
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=PredictionResponse)
async def predict_mental_health(
    request: PredictionRequest,
    current_user: Annotated[UserInDB, Depends(get_current_user)]
):
    # Run prediction
    predicted_class, confidence, probabilities = predictor.predict(request.text)
    
    # Check if suicidal (Class 3)
    is_emergency = (predicted_class == "Suicidal")
    
    # Get recommendations
    recommendations = get_recommendations(predicted_class, is_emergency)
    
    # Save to database
    db = get_database()
    prediction_doc = {
        "user_id": current_user.id,
        "input_text": request.text,
        "predicted_class": predicted_class,
        "confidence": confidence,
        "probabilities": probabilities,
        "is_emergency": is_emergency,
        "created_at": datetime.utcnow()
    }
    
    result = await db.predictions.insert_one(prediction_doc)
    prediction_id = str(result.inserted_id)
    
    return PredictionResponse(
        prediction_id=prediction_id,
        predicted_class=predicted_class,
        confidence=confidence,
        probabilities=probabilities,
        recommendations=recommendations,
        is_emergency=is_emergency,
        created_at=prediction_doc["created_at"]
    )
