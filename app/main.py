from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.session import engine, SessionLocal
from app.api.routes import router as api_router
from app.api.auth import router as auth_router
from app.models import base
from app.core.security import get_password_hash
from sqlalchemy import select
from app.models.user import User

app = FastAPI(title=settings.PROJECT_NAME, version=settings.API_VERSION, openapi_url=f"{settings.API_V1_STR}/openapi.json")

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=list(settings.BACKEND_CORS_ORIGINS),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(base.Base.metadata.create_all)
    # seed demo user
    async with SessionLocal() as session:
        existing = await session.execute(select(User).where(User.email == "demo@example.com"))
        if existing.scalar() is None:
            session.add(User(email="demo@example.com", hashed_password=get_password_hash("demo123"), is_active=True))
            await session.commit()

@app.get("/", summary="Root")
async def root():
    return {"message": "Welcome to the Portfolio Analytics API"}

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(auth_router, prefix=settings.API_V1_STR)
# Analaytics_Backend_FastAPI

An anonymized, production-ready FastAPI backend template for portfolio use. Demonstrates clean async architecture, JWT auth scaffolding, and containerized local development without exposing proprietary logic.

## Features
- FastAPI async application architecture
- PostgreSQL (async SQLAlchemy 2.x) session dependency
- Redis-ready (cache / rate limit stubs)
- JWT auth scaffolding (login token endpoint, password hashing)
- Modular app layout (core, db, models, schemas, api, services)
- Sample analytics endpoint
- Dockerfile & docker-compose (API + Postgres + Redis)
- Alembic migrations folder placeholder
- Basic pytest suite (root & auth)

## Layout
```
app/
  main.py
  core/
    config.py
    security.py
  db/session.py
  models/base.py, user.py
  schemas/user.py, auth.py
  api/routes.py, auth.py
  services/health.py
tests/
  test_root.py
  test_auth.py
```

## Quick Start
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload --port 8000
```
Open http://localhost:8000/docs

## .env Example
```env
PROJECT_NAME=Portfolio Analytics API
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=analytics_db
REDIS_HOST=localhost
REDIS_PORT=6379
BACKEND_CORS_ORIGINS=http://localhost:5173,http://localhost:3000
ACCESS_TOKEN_EXPIRE_MINUTES=60
DEBUG=true
```

## Auth
POST /api/v1/auth/token (form fields: username, password)
Demo seeded user: demo@example.com / demo123

## Docker
```bash
docker compose up --build
```
Services: api (8000), postgres (5432), redis (6379)

## Tests
```bash
pytest -q
```

## Roadmap
- Refresh tokens & user CRUD
- Redis cache wiring
- Alembic revisions sample
- Extended analytics endpoints

## License
MIT

## Disclaimer
All sensitive or proprietary logic removed. Safe for public portfolio publication.

