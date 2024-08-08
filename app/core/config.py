from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    ENV: str = "dev"
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    WORKERS_COUNT: int = 1
    RELOAD: bool = True

    DATABASE_URL: str
    DB_ECHO: bool = False


settings = Settings()  # type: ignore
