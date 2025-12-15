# Job Tracker – Backend (FastAPI)

Job Tracker, kullanıcıların iş başvurularını (Applied / Interview / Offer / Rejected)
takip edebileceği bir uygulamadır.  
Bu repository, projenin **FastAPI + PostgreSQL (Supabase) + JWT Auth** tabanlı backend kısmını içerir.

---

## 🚀 Teknolojiler

- **FastAPI** – REST API
- **PostgreSQL** – Veritabanı (Supabase)
- **SQLAlchemy** – ORM
- **Alembic** – Database migration
- **Supabase Auth** – JWT tabanlı kimlik doğrulama
- **Pydantic** – Request / Response validation

---

## 📁 Proje Yapısı

app/
├── main.py # FastAPI app entrypoint
├── db/
│ ├── database.py # DB connection & session
│ └── deps.py # DB dependency
├── models/
│ ├── user.py # User model
│ └── job.py # JobApplication model + JobStatus enum
├── schemas/
│ ├── user.py # User schemas
│ ├── job.py # Job schemas
│ └── dashboard.py # Dashboard response schema
├── services/
│ ├── auth.py # Auth business logic
│ ├── auth_utils.py # Supabase JWT validation
│ ├── security.py # Password hashing
│ └── job_service.py # Job CRUD logic
├── routers/
│ ├── auth.py # /auth endpoints
│ ├── jobs.py # /jobs endpoints
│ └── dashboard.py # /dashboard endpoints
alembic/
├── versions/ # Migration files
alembic.ini

yaml
Kodu kopyala

---

## 🔐 Authentication

- Authentication Supabase üzerinden yapılır.
- Frontend, Supabase’ten aldığı **JWT access token**’ı
  `Authorization: Bearer <token>` header’ı ile backend’e gönderir.
- Backend tarafında token doğrulaması `get_current_user` ile yapılır.

---

## 📌 API Endpoints

### Auth
- `POST /auth/register`
- `POST /auth/login`

### Jobs
- `POST /jobs`
- `GET /jobs`
- `GET /jobs/{id}`
- `PUT /jobs/{id}`
- `DELETE /jobs/{id}`

### Dashboard
- `GET /dashboard/summary`

---

## 🧱 Job Status (Enum)

Applied
Interview
Offer
Rejected

yaml
Kodu kopyala

- DB seviyesinde PostgreSQL ENUM
- API & Swagger uyumlu

---

## ⚙️ Kurulum

### 1️⃣ Repository’yi klonla
```bash
git clone https://github.com/codeby-nurgul/-Job-tracker.git
cd job-tracker-backend
2️⃣ Virtual environment oluştur
bash
Kodu kopyala
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
3️⃣ Bağımlılıkları yükle
bash
Kodu kopyala
pip install -r requirements.txt
🔑 Ortam Değişkenleri
.env dosyası oluştur:

env
Kodu kopyala
DATABASE_URL=postgresql+psycopg2://<user>:<password>@<host>:5432/<db>
SUPABASE_URL=https://xxxx.supabase.co
SUPABASE_ANON_KEY=your-anon-key
⚠️ .env dosyası gitignore içindedir.

🗄️ Database Migration
Mevcut migration’ları çalıştır:

bash
Kodu kopyala
alembic upgrade head
Yeni migration oluşturmak için:

bash
Kodu kopyala
alembic revision --autogenerate -m "migration message"
▶️ Uygulamayı Çalıştır
bash
Kodu kopyala
uvicorn app.main:app --reload
API: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

📊 Dashboard
GET /dashboard/summary endpoint’i:

Toplam başvuru sayısı

Status bazlı başvuru istatistikleri

Frontend dashboard ve kanban board için hazır yapıdadır.
