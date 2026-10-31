# Claude Code Instructions

This project adheres strictly to the governance and architecture documented in [AGENTS.md](AGENTS.md) and [docs/GOVERNANCE.md](docs/GOVERNANCE.md).

## Critical Non-Negotiables
1. **NO ACTION WITHOUT APPROVAL**: Always present an implementation proposal (files affected, commands, risks) and wait for explicit user approval before modifying code or running mutating commands.
2. **Language Rules**:
   - The user communicates in Hinglish.
   - Respond and explain concepts in conversational Hinglish.
   - All code, variable names, comments, docstrings, commit messages, and documentation files must be written in professional English.
3. **Security**:
   - Never expose credentials or edit `.env` without user consent.
   - Never commit sensitive keys.

## Quick Reference Commands
- Python Environment: `.venv/bin/python`
- Run Server: `.venv/bin/uvicorn app.main:app --reload --port 8000`
- Docker Database: `docker compose up -d postgres`
- Alembic Migration: `.venv/bin/alembic revision --autogenerate -m "message"`
- Apply Migration: `.venv/bin/alembic upgrade head`

## Full System Context
See [AGENTS.md](AGENTS.md) for full architecture, active database state, and design principles.
