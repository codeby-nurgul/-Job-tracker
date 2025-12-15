from pydantic import BaseModel
from datetime import date
from uuid import UUID
from enum import Enum


class JobStatus(str, Enum):
    Applied = "Applied"
    Interview = "Interview"
    Offer = "Offer"
    Rejected = "Rejected"


class JobCreate(BaseModel):
    company_name: str
    position: str
    status: JobStatus = JobStatus.Applied
    apply_date: date | None = None
    job_link: str | None = None
    notes: str | None = None


class JobUpdate(BaseModel):
    company_name: str | None = None
    position: str | None = None
    status: JobStatus | None = None
    apply_date: date | None = None
    job_link: str | None = None
    notes: str | None = None


class JobOut(BaseModel):
    id: UUID
    company_name: str
    position: str
    status: JobStatus
    apply_date: date
    job_link: str | None
    notes: str | None

    class Config:
        from_attributes = True
