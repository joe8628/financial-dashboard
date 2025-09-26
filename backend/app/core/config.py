import os
from typing import List
from pydantic import PostgresDsn

from pydantic_settings import BaseSettings, PydanticBaseSettingsSource

class Settings(BaseSettings):
    # Database
    database_url: str = os.getenv("DATABASE_URL", "postgresql://postgres:tor@localhost:5433/financial_dashboard")
    
    # Security
    secret_key: str = os.getenv("SECRET_KEY", "your-super-secret-key-change-this-in-production")
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS
    allowed_origins: List[str] = ["http://localhost:3000"]
    
    # App
    app_name: str = "Financial Dashboard API"
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    
    class Config:
        env_file = ".env"

settings = Settings()