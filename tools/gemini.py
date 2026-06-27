"""Shared Google Gemini client for EduForge."""

from __future__ import annotations

import json
from functools import lru_cache
from typing import Any

from google import genai
from google.genai.types import GenerateContentConfig

from config import settings


@lru_cache(maxsize=1)
def get_client() -> genai.Client:
    """
    Create and cache a single Gemini client instance.

    Returns:
        Configured Google Gen AI client.
    """
    settings.validate()

    return genai.Client(api_key=settings.google_api_key)


@lru_cache(maxsize=1)
def get_model_name() -> str:
    """Return the configured Gemini model name."""
    return settings.gemini_model


def generate_text(
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.3,
) -> str:
    """
    Generate plain text using Gemini.

    Args:
        system_prompt: System instructions.
        user_prompt: User input.
        temperature: Sampling temperature.

    Returns:
        Generated text.
    """

    client = get_client()

    response = client.models.generate_content(
        model=get_model_name(),
        contents=user_prompt,
        config=GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=temperature,
        ),
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    return response.text.strip()


def generate_json(
    system_prompt: str,
    user_prompt: str,
    temperature: float = 0.2,
) -> dict[str, Any]:
    """
    Generate structured JSON from Gemini.

    The prompt should explicitly instruct the model to return only JSON.

    Args:
        system_prompt: System instructions.
        user_prompt: User prompt.
        temperature: Sampling temperature.

    Returns:
        Parsed JSON dictionary.

    Raises:
        ValueError: If the model does not return valid JSON.
    """

    text = generate_text(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        temperature=temperature,
    )

    # Remove Markdown code fences if present.
    cleaned = text.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]

    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]

    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)

    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Gemini returned invalid JSON:\n{cleaned}"
        ) from exc