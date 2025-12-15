from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserOut(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

