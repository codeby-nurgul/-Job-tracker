from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional


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

class ProfileSettingsUpdate(BaseModel):
    language: Optional[str]
    timezone: Optional[str]
    default_job_status: Optional[str]