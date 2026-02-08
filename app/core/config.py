from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str
    
    # App
    DEBUG: bool = True
    
    # Rate limiting (we'll add more later)
    RATE_LIMIT_PER_HOUR: int = 50
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Create settings instance
settings = Settings()