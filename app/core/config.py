from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str | None = None
    SARVAM_API_KEY: str | None = None
    GROK_API_KEY: str | None = None
    GROQ_API_KEY: str | None = None
    SARVAM_BASE_URL : str | None = None
        
    ENV: str = "local"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        
@lru_cache()
def get_settings():
    return Settings()

