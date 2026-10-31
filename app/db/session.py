from collections.abc import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

# Normalize DATABASE_URL for psycopg (v3) if needed
db_url = settings.DATABASE_URL
if db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql+psycopg://", 1)
elif db_url.startswith("postgresql://") and not db_url.startswith("postgresql+"):
    db_url = db_url.replace("postgresql://", "postgresql+psycopg://", 1)

from app.db.guard import setup_database_guard

# SQLAlchemy engine with connection pool configurations
engine = create_engine(
    db_url,
    pool_pre_ping=True,  # Proactively verifies connection liveness before checkout
    pool_size=10,        # Number of permanent connections maintained in the pool
    max_overflow=20,     # Max extra connections allowed under heavy load
)

# Attach security guard to intercept destructive operations
setup_database_guard(engine)

# Factory for creating database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db() -> Generator[Session, None, None]:
    """Dependency that provides a transactional database session per request.

    Ensures the session is always closed after the request completes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
