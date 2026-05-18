from fastapi import APIRouter, Depends
from typing import Annotated, List
from ...models.user import UserInDB
from .auth import get_current_user
from ...database import get_database

router = APIRouter()

@router.get("/history")
async def get_history(
    current_user: Annotated[UserInDB, Depends(get_current_user)],
    limit: int = 50
):
    db = get_database()
    cursor = db.predictions.find({"user_id": current_user.id}).sort("created_at", -1).limit(limit)
    history = await cursor.to_list(length=limit)
    
    # Format for response
    for item in history:
        item["_id"] = str(item["_id"])
    return history

@router.get("/stats")
async def get_stats(
    current_user: Annotated[UserInDB, Depends(get_current_user)]
):
    db = get_database()
    pipeline = [
        {"$match": {"user_id": current_user.id}},
        {"$group": {"_id": "$predicted_class", "count": {"$sum": 1}}}
    ]
    cursor = db.predictions.aggregate(pipeline)
    results = await cursor.to_list(length=None)
    
    stats = {"Normal": 0, "Anxiety": 0, "Depression": 0, "Suicidal": 0}
    for res in results:
        stats[res["_id"]] = res["count"]
        
    return stats
