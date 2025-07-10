from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Starter"
    ADMIN_EMAIL: str | None = None
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT_JSON: bool = True

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
