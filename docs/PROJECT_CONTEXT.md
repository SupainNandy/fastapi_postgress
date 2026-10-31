# Project Context

## Overview
This repository contains a production-oriented RESTful API built with **FastAPI** and **PostgreSQL**. The primary architectural focus is demonstrating professional software engineering standards, clean architecture, resilient database management with **SQLAlchemy 2.0**, automated migrations using **Alembic**, connection pooling via **Psycopg 3**, and containerized infrastructure via **Docker Compose**.

## Core Technology Stack
- **Framework**: FastAPI (0.162+)
- **Server**: Uvicorn (0.54+)
- **Database**: PostgreSQL 16 (running via Docker)
- **Database Driver**: Psycopg 3 (`psycopg`, `psycopg-binary`)
- **ORM**: SQLAlchemy 2.0 (Typed `Mapped` & `mapped_column`)
- **Schema & Validation**: Pydantic v2 & Pydantic-Settings
- **Database Migrations**: Alembic (1.20+)
- **Environment & Secret Management**: `python-dotenv` & `.env` / `.env.example`

## Key Capabilities
1. **Strict Separation of Concerns**: Clean layers separating configuration, database sessions, domain models, Pydantic schemas, and API endpoints.
2. **Resilient Connection Pooling**: SQLAlchemy configured with `pool_pre_ping=True`, permanent connection pooling, and overflow management.
3. **Automated Migrations**: Version-controlled database schema migrations tracking all model alterations.
4. **Production Readiness**: Docker Compose orchestration for PostgreSQL and pgAdmin, parameterized via environment variables.
