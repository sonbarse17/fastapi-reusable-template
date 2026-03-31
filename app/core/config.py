"""
Application Configuration (config.py)
=====================================
Loads environment variables and configuration settings utilizing Pydantic's BaseSettings. 
Pydantic ensures that if `DEBUG` should be a boolean, an error triggers on boot if `.env`
has `DEBUG="random_string"`.
"""

from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment or .env file."""
    # App
    PROJECT_NAME: str = "FastAPI Phase2 App"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    BACKEND_CORS_ORIGINS: list[str] = ["http://localhost", "http://localhost:8000", "http://localhost:3000"]


    # Security
    SECRET_KEY: str = "supersecretkey-change-in-production"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    # DB setup
    # Using SQLite for local testing as per Phase-2 prompt choice
    DATABASE_URL: str = "sqlite:///./sql_app.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


# Instantiate settings to be imported across the application
settings = Settings()
