from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, field_validator
from typing import Any, List
import secrets

class Settings(BaseSettings):
    API_VERSION: str = "v1"
    API_V1_STR: str = f"/api/{API_VERSION}"
    PROJECT_NAME: str = "Portfolio Analytics API"
    DEBUG: bool = True

    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_NAME: str = "analytics_db"

    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    BACKEND_CORS_ORIGINS: List[str] = []
    ASYNC_DATABASE_URI: str | None = None

    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"

    @field_validator("ASYNC_DATABASE_URI", mode="before")
    def build_db_uri(cls, v: str | None, values: dict[str, Any]):
        if v:
            return v
        return str(PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values["DATABASE_USER"],
            password=values["DATABASE_PASSWORD"],
            host=values["DATABASE_HOST"],
            port=str(values["DATABASE_PORT"]),
            path=values["DATABASE_NAME"],
        ))

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
