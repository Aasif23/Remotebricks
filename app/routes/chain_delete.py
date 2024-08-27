from fastapi import APIRouter, HTTPException
from database import users_collection, linked_ids_collection

router = APIRouter()

@router.delete("/delete-user/{user_email}")
async def delete_user(user_email: str):
    user = users_collection.find_one({"email": user_email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    users_collection.delete_one({"_id": user["_id"]})
    linked_ids_collection.delete_many({"user_id": user["_id"]})
    
    return {"message": "User and all associated data deleted successfully"}
