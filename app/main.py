from fastapi import FastAPI
from app.routers.auth import router as auth_router
from app.routers.users_router import router as users_router
from app.routers.jobs import router as jobs_router
from app.routers.dashboard import router as dashboard_router

app = FastAPI(title="Job Tracker API")

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(jobs_router)
app.include_router(dashboard_router)

@app.get("/")
def root():
    return {"status": "ok"}
