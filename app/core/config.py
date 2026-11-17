from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    project_name: str = "website API"
    database_url: str 
    debug: bool = True
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()