from fastapi import APIRouter, HTTPException
from models import User
from models import LoginData
from database import users_collection
import bcrypt

router = APIRouter()

@router.post("/register")
async def register_user(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user_data = user.dict()
    user_data["password"] = hashed_password

    users_collection.insert_one(user_data)
    return {"message": "User registered successfully"}


@router.post("/login")
async def login_user(data: LoginData):
    user = users_collection.find_one({"email": data.email})
    
    if not user or not bcrypt.checkpw(data.password.encode('utf-8'), user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful"}
