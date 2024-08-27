from fastapi import APIRouter , HTTPException
from database import users_collection, linked_ids_collection

router = APIRouter()

@router.get("/user-linked-ids/{user_email}")
async def get_user_linked_ids(user_email: str):
    user = users_collection.find_one({"email": user_email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    linked_ids = linked_ids_collection.find({"user_id": user["_id"]})
    return {"user_email": user_email, "linked_ids": [link["linked_id"] for link in linked_ids]}
