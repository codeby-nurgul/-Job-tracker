from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.db.deps import get_db
from app.services.auth_utils import get_current_user
from app.schemas.profile import ProfileUpdate ,ProfileSettingsUpdate
from app.services.profile_service import get_profile, update_profile,get_profile_stats,get_profile_activity, get_goals
from app.models.user import User

router = APIRouter(prefix="/profile", tags=["Profile"])


@router.get("")
def read_profile(
    user: User = Depends(get_current_user)
):
    return get_profile(user)


@router.put("")
def edit_profile(
    data: ProfileUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    updated_user = update_profile(db, user, data)
    return {
        "message": "Profile updated successfully",
        "avatar_url": updated_user.avatar_url
    }

@router.get("/stats")
def profile_stats(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_profile_stats(db, user)

@router.get("/activity")
def profile_activity(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_profile_activity(db, user)

@router.put("/settings")
def update_settings(
    data: ProfileSettingsUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    for k, v in data.dict(exclude_unset=True).items():
        setattr(user, k, v)

    db.commit()
    return {"message": "Settings updated"}

@router.get("/goals")
def read_goals(user: User = Depends(get_current_user)):
    return get_goals(user)


@router.put("/goals")
def update_goals(
    goal: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    user.monthly_application_goal = goal
    user.last_activity_at = datetime.utcnow()
    db.commit()
    return {"message": "Goal updated"}