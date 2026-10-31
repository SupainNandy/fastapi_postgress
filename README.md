# FastAPI + PostgreSQL Production Backend

A production-ready REST API built with **FastAPI**, **PostgreSQL 16**, **SQLAlchemy 2.0**, and **Alembic**, following clean architecture principles.

---

## Architecture Overview

```text
app/
├── core/         # App settings & environment loader
├── db/           # Engine, connection pooling, SessionLocal, get_db
├── models/       # SQLAlchemy 2.0 ORM models
├── schemas/      # Pydantic v2 validation DTOs
├── api/          # Route definitions (v1)
└── main.py       # FastAPI application entrypoint
```

---

## Quick Start Guide

### 1. Configure Environment Variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

### 2. Start PostgreSQL Container
Start PostgreSQL and pgAdmin using Docker Compose:
```bash
docker compose up -d postgres
```

### 3. Apply Database Migrations
Run Alembic to apply schema migrations to PostgreSQL:
```bash
.venv/bin/alembic upgrade head
```

### 4. Run Development Server
Start the FastAPI server with Uvicorn:
```bash
.venv/bin/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Interactive API Documentation
* **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)
* **Health Check**: [http://localhost:8000/health](http://localhost:8000/health)

---

## Detailed Documentation
* [Architecture Guidelines](docs/ARCHITECTURE.md)
* [Database & Connection Pooling Guide](docs/DATABASE.md)
* [Project Context & Decisions](docs/PROJECT_CONTEXT.md)
* [Task Tracker](docs/TASK_TRACKER.md)
