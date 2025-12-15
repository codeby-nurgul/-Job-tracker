from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from app.models.job import JobStatus

from app.db.deps import get_db
from app.schemas.job import JobCreate, JobUpdate, JobOut
from app.services.job_service import (
    create_job, get_jobs, get_job, update_job, delete_job
)
from app.services.auth_utils import get_current_user

router = APIRouter(prefix="/jobs", tags=["Jobs"])


@router.post("", response_model=JobOut)
def create(
    data: JobCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return create_job(db, user.id, data)


@router.get("", response_model=list[JobOut])
def list_jobs(
    status: JobStatus | None = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    return get_jobs(
        db=db,
        user_id=user.id,
        status=status,
        page=page,
        limit=limit
    )



@router.get("/{job_id}", response_model=JobOut)
def detail(
    job_id: UUID,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    job = get_job(db, job_id, user.id)
    if not job:
        raise HTTPException(404, "Job not found")
    return job


@router.put("/{job_id}", response_model=JobOut)
def update(
    job_id: UUID,
    data: JobUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    job = get_job(db, job_id, user.id)
    if not job:
        raise HTTPException(404, "Job not found")
    return update_job(db, job, data)


@router.delete("/{job_id}")
def remove(
    job_id: UUID,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    job = get_job(db, job_id, user.id)
    if not job:
        raise HTTPException(404, "Job not found")
    delete_job(db, job)
    return {"message": "Deleted"}
