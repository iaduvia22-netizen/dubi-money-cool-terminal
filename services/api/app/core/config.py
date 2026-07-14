from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "local"
    cors_origins: str = "http://localhost:3000"
    enable_live_trading: bool = False
    enable_ctrader_demo: bool = False
    enable_ai_explanations: bool = False
    enable_billing: bool = False

    class Config:
        env_file = ".env"
        extra = "ignore"


@lru_cache
def get_settings() -> Settings:
    return Settings()
