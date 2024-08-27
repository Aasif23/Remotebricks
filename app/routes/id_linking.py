from fastapi import APIRouter, HTTPException
from database import users_collection, linked_ids_collection
from pydantic import BaseModel

router = APIRouter()

class LinkID(BaseModel):
    user_email: str
    id_to_link: str

@router.post("/link-id")
async def link_id(data: LinkID):
    user = users_collection.find_one({"email": data.user_email})
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    linked_ids_collection.insert_one({"user_id": user["_id"], "linked_id": data.id_to_link})
    return {"message": "ID linked successfully"}
