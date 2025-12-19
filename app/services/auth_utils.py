from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from supabase import create_client
import os
import uuid

from app.db.deps import get_db
from app.models.user import User

security = HTTPBearer()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_ANON_KEY")
)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    token = credentials.credentials

    auth_response = supabase.auth.get_user(token)

    if not auth_response or not auth_response.user:
        raise HTTPException(status_code=401, detail="Invalid token")

    supabase_user_id = uuid.UUID(auth_response.user.id)

    user = (
        db.query(User)
        .filter(User.id == supabase_user_id)
        .first()
    )

    if not user:
        raise HTTPException(status_code=404, detail="User not found in database")

    return user

