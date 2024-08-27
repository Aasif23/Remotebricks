from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginData(BaseModel):
    email: str
    password: str