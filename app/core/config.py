from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application runtime settings loaded from environment variables."""

    PROJECT_NAME: str = "FastAPI PostgreSQL Application"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = (
        "postgresql+psycopg://postgres:FastApi@123@localhost:5432/fastapi_db"
    )

    # Security (For future auth integration)
    SECRET_KEY: str = "temporary_dev_secret_key_change_in_production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
