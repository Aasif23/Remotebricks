from fastapi import APIRouter, HTTPException
from models import User
from models import LoginData
from database import users_collection
import bcrypt

# Define a router for authentication-related endpoints
router = APIRouter()

@router.post("/register")
async def register_user(user: User):

    # Check if the email is already registered
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the user's password
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    # Prepare the user data for insertion
    user_data = user.dict()
    user_data["password"] = hashed_password

    # Insert the user data into the users collection
    users_collection.insert_one(user_data)
    return {"message": "User registered successfully"}


@router.post("/login")
async def login_user(data: LoginData):

    # Find the user by email
    user = users_collection.find_one({"email": data.email})
    
    # Validate the password
    if not user or not bcrypt.checkpw(data.password.encode('utf-8'), user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful"}
