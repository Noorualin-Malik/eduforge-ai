"""Application configuration."""

from __future__ import annotations

import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    def __init__(self) -> None:
        self.google_api_key: str = os.getenv("GOOGLE_API_KEY", "").strip()
        self.tavily_api_key: str = os.getenv("TAVILY_API_KEY", "").strip()

        self.gemini_model: str = "gemini-2.5-flash"

        self.chroma_path: str = "./chroma_db"

    @property
    def google_configured(self) -> bool:
        """Return True if the Google API key exists."""
        return bool(self.google_api_key)

    @property
    def tavily_configured(self) -> bool:
        """Return True if the Tavily API key exists."""
        return bool(self.tavily_api_key)

    def validate(self) -> None:
        """Validate required configuration."""

        missing: list[str] = []

        if not self.google_configured:
            missing.append("GOOGLE_API_KEY")

        if not self.tavily_configured:
            missing.append("TAVILY_API_KEY")

        if missing:
            raise EnvironmentError(
                "Missing required environment variable(s): "
                + ", ".join(missing)
            )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()


settings = get_settings()