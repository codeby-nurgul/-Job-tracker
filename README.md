# Job Tracker – Backend (FastAPI)

- Job Tracker is an application that allows users to track their job applications across different stages (Applied / Interview / Offer / Rejected).

- This repository contains the backend of the project, built with
FastAPI + PostgreSQL (Supabase) + JWT Authentication.

---

## Technologies

- **FastAPI** – REST API
- **PostgreSQL** – Database(Supabase)
- **SQLAlchemy** – ORM
- **Alembic** – Database migration
- **Supabase Auth** – JWT based Authentication
- **Pydantic** – Request / Response validation

--- 

## Authentication

- Authentication is handled via Supabase.

- The frontend sends the JWT access token obtained from Supabase to the backend using the
Authorization: Bearer <token> header.

- On the backend, token validation is performed using the get_current_user dependency.

---

##  - API Endpoints

### Auth
- POST /auth/register
- POST /auth/login

### Jobs
- POST /jobs
- GET /jobs
- GET /jobs/{id}
- PUT /jobs/{id}
- DELETE /jobs/{id}

### Dashboard
- GET /dashboard/summary

---

## Job Status (Enum)

Applied
Interview
Offer
Rejected

---

## Setup & Installation


### 
```bash
1️⃣ Clone the Repository
git clone https://github.com/codeby-nurgul/-Job-tracker.git

cd -Job-tracker

2️⃣ Create virtual environment 
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Load the dependencies
pip install -r requirements.txt

---

Environment Variables
Create .env file :
DATABASE_URL=postgresql+psycopg2://<user>:<password>@<host>:5432/<db>
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_ANON_KEY=your-anon-key


▶️ Run backend 

uvicorn app.main:app --reload
```
- API: http://127.0.0.1:8000

- Swagger UI: http://127.0.0.1:8000/docs

#### Run Frontend :
1) cd Job-Tracker-UI 
2) npm install
3) npm run dev

---



