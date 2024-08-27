from fastapi import APIRouter, HTTPException
from database import users_collection, linked_ids_collection
from pydantic import BaseModel
from models import LinkID

# Define a router for ID linking-related endpoints
router = APIRouter()


@router.post("/link-id")
async def link_id(data: LinkID):

    # Find the user by email
    user = users_collection.find_one({"email": data.user_email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Insert the linked ID into the linked_ids collection
    linked_ids_collection.insert_one({"user_id": user["_id"], "linked_id": data.id_to_link})
    return {"message": "ID linked successfully"}
