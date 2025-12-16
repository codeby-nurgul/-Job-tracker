from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.users_router import router as users_router
from app.routers.jobs import router as jobs_router
from app.routers.dashboard import router as dashboard_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Job Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # React (Vite)
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(jobs_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"status": "ok"}
