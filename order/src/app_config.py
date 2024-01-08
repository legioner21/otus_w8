from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    PROJECT_NAME: str = "otus-8-order"
    API_VSTR: str = "/api/v1"
    ORDER_PAYMENT_URL: str = Field(..., env="ORDER_PAYMENT_URL")
    ORDER_ROLLBACK_PAYMENT_URL: str = Field(..., env="ORDER_ROLLBACK_PAYMENT_URL")
    ORDER_RESERVE_URL: str = Field(..., env="ORDER_RESERVE_URL")
    ORDER_ROLLBACK_RESERVE_URL: str = Field(..., env="ORDER_ROLLBACK_RESERVE_URL")
    ORDER_DELIVERY_URL: str = Field(..., env="ORDER_DELIVERY_URL")
    ORDER_ROLLBACK_DELIVERY_URL: str = Field(..., env="ORDER_ROLLBACK_DELIVERY_URL")

    class Config:
        env_file = ".env"


settings = Settings()
