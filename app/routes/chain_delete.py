from fastapi import APIRouter, HTTPException
from database import users_collection, linked_ids_collection

# Define a router for chain delete-related endpoints
router = APIRouter()

@router.delete("/delete-user/{user_email}")
async def delete_user(user_email: str):
    # Find the user by email
    user = users_collection.find_one({"email": user_email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete the user from the users collection
    users_collection.delete_one({"_id": user["_id"]})

     # Delete all linked IDs associated with the user's account
    linked_ids_collection.delete_many({"user_id": user["_id"]})
    
    return {"message": "User and all associated data deleted successfully"}
