from sqlalchemy import Column, String, Date, Text, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
import enum

from app.db.database import Base


class JobStatus(enum.Enum):
    Applied = "Applied"
    Interview = "Interview"
    Offer = "Offer"
    Rejected = "Rejected"


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)

    company_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    status = Column(Enum(JobStatus, name="jobstatus"), nullable=False)

    apply_date = Column(Date, server_default=func.current_date())
    job_link = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
