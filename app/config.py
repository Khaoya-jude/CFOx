# Global configuration settings for the CFOx application.

from pydantic import BaseModel
from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseModel, BaseSettings):
    APP_NAME: str = "CFOx"
    ENV: str = os.getenv("ENV", "dev")

    # MCP
    MCP_HOST: str = os.getenv("MCP_HOST", "0.0.0.0")
    MCP_PORT: int = int(os.getenv("MCP_PORT", 3333))

    # Database
    POSTGRES_URL: str | None = os.getenv("POSTGRES_URL")

    # Vector DB
    VECTOR_DB_URL: str | None = os.getenv("VECTOR_DB_URL")

    # Security
    ENABLE_AUDIT_LOGS: bool = True
    MAX_AUTONOMOUS_OUTFLOW: float = float(
        os.getenv("MAX_AUTONOMOUS_OUTFLOW", 50_000)
    )

    openai_api_key: str | None = None
    llm_model: str = "gpt-4o-mini"

    class Config:
        env_file = ".env"

settings = Settings()
