from sqlalchemy.orm import Session
from uuid import UUID

from app.models.job import JobApplication
from app.schemas.job import JobCreate, JobUpdate
from app.models.job import JobStatus


def create_job(db: Session, user_id: UUID, data: JobCreate):
    job = JobApplication(
        user_id=user_id,
        **data.dict(exclude_unset=True)
    )
    db.add(job)
    db.commit()
    db.refresh(job)
    return job


def get_jobs(
    db: Session,
    user_id: UUID,
    status: JobStatus | None = None,
    page: int = 1,
    limit: int = 10
):
    query = db.query(JobApplication).filter(
        JobApplication.user_id == user_id
    )

    if status:
        query = query.filter(JobApplication.status == status)

    return (
        query
        .order_by(JobApplication.apply_date.desc())
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )


def get_job(db: Session, job_id: UUID, user_id: UUID):
    return db.query(JobApplication).filter(
        JobApplication.id == job_id,
        JobApplication.user_id == user_id
    ).first()


def update_job(db: Session, job: JobApplication, data: JobUpdate):
    for field, value in data.dict(exclude_unset=True).items():
        setattr(job, field, value)

    db.commit()
    db.refresh(job)
    return job


def delete_job(db: Session, job: JobApplication):
    db.delete(job)
    db.commit()
