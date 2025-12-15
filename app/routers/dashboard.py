from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.deps import get_db
from app.models.job import JobApplication
from app.services.auth_utils import get_current_user
from app.schemas.dashboard import DashboardSummary
from sqlalchemy import func

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/summary", response_model=DashboardSummary)
def dashboard_summary(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    total = (
        db.query(func.count(JobApplication.id))
        .filter(JobApplication.user_id == user.id)
        .scalar()
    )

    rows = (
        db.query(
            JobApplication.status,
            func.count(JobApplication.id)
        )
        .filter(JobApplication.user_id == user.id)
        .group_by(JobApplication.status)
        .all()
    )

    status_counts = {status.value: count for status, count in rows}

    return {
        "total_applications": total,
        "status_counts": status_counts
    }
