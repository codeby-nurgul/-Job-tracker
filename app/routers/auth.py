from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserLogin
from app.services.auth import register_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(data: UserCreate):
    res = register_user(data.email, data.password)

    if res.user is None:
        raise HTTPException(status_code=400, detail="Registration failed")

    return {
        "id": res.user.id,
        "email": res.user.email
    }


@router.post("/login")
def login(data: UserLogin):
    res = authenticate_user(data.email, data.password)

    if res.session is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {
        "access_token": res.session.access_token,
        "token_type": "bearer",
        "user": {
            "id": res.user.id,
            "email": res.user.email
        }
    }
