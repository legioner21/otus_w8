from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PROJECT_NAME: str = "otus-8-delivery"
    API_VSTR: str = "/api/v1"

    class Config:
        env_file = ".env"


settings = Settings()
