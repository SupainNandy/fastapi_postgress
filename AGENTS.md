# Universal AI Agent Guide (AGENTS.md)

This document is the primary repository guide for any AI coding agent (Antigravity, Claude Code, Cursor, Copilot, Codex, etc.). Read this before executing any action.

---

## 1. Governance & Strict Non-Negotiable Rules

* **Single Source of Truth**: All rules are governed by [`docs/GOVERNANCE.md`](file:///home/supain/SupainNandy/FastApi_Postgress/docs/GOVERNANCE.md).
* **NO ACTION WITHOUT EXPLICIT APPROVAL**:
  - Never create, edit, delete, or rename files without proposing the exact changes and waiting for user approval.
  - Never install packages, modify `requirements.txt`, run migrations, or execute mutating shell commands without prior permission.
* **Communication Rules**:
  - The user communicates in Hinglish (Hindi + English).
  - All chat responses and technical explanations must be given in conversational, clear Hinglish.
  - All source code, identifiers, comments, commit messages, and documentation files (`docs/*.md`, `README.md`) must be written in professional English. Never generate Hindi or Hinglish inside the codebase.
* **Security Rules**:
  - Never hardcode secrets or commit `.env`.
  - Always validate incoming inputs using Pydantic schemas.
  - Always use SQLAlchemy 2.0 parameterized queries to prevent SQL injection.

---

## 2. Project Architecture & Layout

The project follows a Clean Layered Architecture:

```text
FastApi_Postgress/
├── .env                  # Local secrets (gitignored)
├── .env.example          # Safe template for environment variables
├── docker-compose.yml    # PostgreSQL 16 & pgAdmin services
├── requirements.txt      # Pinned dependencies
├── alembic.ini           # Alembic configuration
├── alembic/              # Database migration scripts
│   ├── env.py            # Dynamically loads DB_URL and app.db.base.Base metadata
│   └── versions/         # Migration versions (e.g. d7fc2046d608_create_todos_table.py)
├── docs/                 # Authoritative documentation
│   ├── GOVERNANCE.md     # Primary agent rules
│   ├── ARCHITECTURE.md   # System design & layer communication
│   ├── DATABASE.md       # PostgreSQL pooling & Alembic guide
│   ├── PROJECT_CONTEXT.md# Tech stack & capabilities
│   └── TASK_TRACKER.md   # Completed and planned milestones
└── app/
    ├── main.py           # FastAPI app instance, CORS, routers, lifespan
    ├── core/
    │   └── config.py     # Pydantic-Settings environment loader
    ├── db/
    │   ├── base.py       # SQLAlchemy 2.0 DeclarativeBase
    │   └── session.py    # Engine with pool_pre_ping=True, SessionLocal, get_db()
    ├── models/
    │   ├── __init__.py   # Model registry for Alembic discovery
    │   └── todo.py       # Todo SQLAlchemy 2.0 table definition (Mapped columns)
    ├── schemas/
    │   ├── __init__.py   # DTO exports
    │   └── todo.py       # Pydantic v2 schemas (TodoCreate, TodoUpdate, TodoResponse)
    └── api/
        ├── __init__.py
        └── v1/
            ├── __init__.py # Router aggregator
            └── endpoints/
                └── todos.py # Todo CRUD API routes with Depends(get_db)
```

---

## 3. Active Database & Infrastructure State

* **Database Engine**: PostgreSQL 16 container running via Docker Compose (`postgres_db`).
* **Connection String**: `postgresql+psycopg://postgres:FastApi@123@localhost:5432/fastapi_db`
* **Driver**: Psycopg 3 (`psycopg`, `psycopg-binary`).
* **Alembic State**: Migrations applied (`d7fc2046d608_create_todos_table`, `61f78504b179_create_students_table`). Active tables: `alembic_version`, `todos`, `students`.
* **Database Guard**: Active hooks in `.agents/hooks.json` and `app/db/guard.py` blocking unauthorized `DROP`, `TRUNCATE`, and destructive schema operations.

---

## 4. Key Developer Commands

All commands should use the project virtual environment (`.venv`):

* **Run Development Server**:
  ```bash
  .venv/bin/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```
* **Start PostgreSQL Container**:
  ```bash
  docker compose up -d postgres
  ```
* **Check Container Status**:
  ```bash
  docker compose ps
  ```
* **Generate Database Migration**:
  ```bash
  .venv/bin/alembic revision --autogenerate -m "describe_migration"
  ```
* **Apply Database Migrations**:
  ```bash
  .venv/bin/alembic upgrade head
  ```

---

## 5. Mandatory Agent Workflow for Every Task

1. **Understand**: Read user instruction (in Hinglish) and cross-reference with existing code.
2. **Analyze**: Check architecture, dependencies, security implications.
3. **Propose**: State what will change, why, affected files, commands, and potential risks.
4. **Wait for Approval**: Do not execute or write any code without explicit approval.
5. **Implement**: Execute only what was approved.
6. **Validate**: Run automated checks and tests to verify correctness.
7. **Document**: Update relevant files in `docs/` (especially `TASK_TRACKER.md`).
8. **Report**: Summarize implementation in clear Hinglish.
