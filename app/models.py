from pydantic import BaseModel, EmailStr

# Pydantic model representing the user data
class User(BaseModel):
    username: str
    email: EmailStr # Email field with validation
    password: str   # Plain text password (to be hashed before storing)

# Pydantic model representing the login data
class LoginData(BaseModel):
    email: str         
    password: str      # Plain text password (to be hashed before storing)

# Pydantic model for linking an ID
class LinkID(BaseModel):
    user_email: str     # Email of the user to link the ID to
    id_to_link: str     # ID to be linked to the user's account