from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime)
    language = Column(String, default="tr")
    timezone = Column(String, default="Europe/Istanbul")
    default_job_status = Column(String, default="Applied")
    monthly_application_goal = Column(Integer, default=0)
    last_activity_at = Column(DateTime)

