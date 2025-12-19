from pydantic import BaseModel
from typing import Optional

class ProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    title: Optional[str] = None
    location: Optional[str] = None
    about: Optional[str] = None
    avatar_url: Optional[str] = None

class ProfileSettingsUpdate(BaseModel):
    language: Optional[str] = None
    timezone: Optional[str] = None
    default_job_status: Optional[str] = None