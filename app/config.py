from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str ="MarketMind Intelligence"
    debug: bool = True

    class config:
        env_file = ".env"

settings = Settings()