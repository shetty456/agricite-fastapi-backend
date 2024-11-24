from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    # General settings
    app_name: str = "FastAPI Project"
    debug: bool = True

    # CORS settings
    allowed_origins: List[str] = ["http://localhost", "http://localhost:3000"]

    # Database settings
    database_url: str = (
        "sqlite:///./db.sqlite3"  # SQLite database file in the current directory
    )
    test_database_url: str = (
        "sqlite:///./test_db.sqlite3"  # Separate database for testing
    )
    prod_database_url: str = "postgres://user:password@localhost/dbname"

    # Rate limiting (placeholder)
    rate_limit: int = 100  # 100 requests per minute

    class Config:
        env_file = ".env"


settings = Settings()
