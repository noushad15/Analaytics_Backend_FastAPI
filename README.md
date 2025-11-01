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

