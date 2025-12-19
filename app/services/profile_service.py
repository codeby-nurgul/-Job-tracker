from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.user import User
from app.schemas.profile import ProfileUpdate
from app.models.job import JobApplication, JobStatus

from datetime import datetime

def get_profile(user: User) -> User:
    return user


def update_profile(
    db: Session,
    user: User,
    data: ProfileUpdate
) -> User:
    for field, value in data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user

def get_profile_stats(db: Session, user: User):
    total = (
        db.query(func.count(JobApplication.id))
        .filter(JobApplication.user_id == user.id)
        .scalar()
    )

    def count(status):
        return (
            db.query(func.count(JobApplication.id))
            .filter(
                JobApplication.user_id == user.id,
                JobApplication.status == status
            )
            .scalar()
        )

    interview = count(JobStatus.Interview)
    offer = count(JobStatus.Offer)

    return {
        "total_applications": total,
        "applied": count(JobStatus.Applied),
        "interview": interview,
        "offer": offer,
        "rejected": count(JobStatus.Rejected),
        "interview_rate": round((interview / total) * 100, 2) if total else 0,
        "offer_rate": round((offer / total) * 100, 2) if total else 0
    }


def get_profile_activity(db: Session, user: User):
    jobs = (
        db.query(JobApplication)
        .filter(JobApplication.user_id == user.id)
        .order_by(JobApplication.apply_date.desc())
        .limit(10)
        .all()
    )

    return [
        {
            "company_name": j.company_name,
            "position": j.position,
            "status": j.status.value,
            "apply_date": j.apply_date
        }
        for j in jobs
    ]


def get_goals(user: User):
    return {
        "monthly_application_goal": user.monthly_application_goal,
        "last_activity_at": user.last_activity_at
    }