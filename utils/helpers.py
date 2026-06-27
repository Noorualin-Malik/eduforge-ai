"""Common helper utilities for EduForge."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_prompt(path: str | Path) -> str:
    """
    Load a prompt file.

    Args:
        path: Path to the prompt file.

    Returns:
        Prompt contents as a string.
    """
    return Path(path).read_text(encoding="utf-8").strip()


def strip_code_fences(text: str) -> str:
    """
    Remove Markdown code fences from LLM output.

    Args:
        text: Raw model response.

    Returns:
        Cleaned text.
    """
    cleaned = text.strip()

    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]

    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]

    return cleaned.strip()


def parse_json(text: str) -> dict[str, Any]:
    """
    Parse a JSON string after removing Markdown code fences.

    Args:
        text: JSON string returned by the model.

    Returns:
        Parsed dictionary.

    Raises:
        ValueError: If the JSON is invalid.
    """
    cleaned = strip_code_fences(text)

    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        raise ValueError("Invalid JSON returned by the model.") from exc

    if not isinstance(data, dict):
        raise ValueError("Expected a JSON object.")

    return data


def pretty_json(data: dict[str, Any]) -> str:
    """
    Convert a dictionary to formatted JSON.

    Args:
        data: Dictionary to serialize.

    Returns:
        Pretty-printed JSON string.
    """
    return json.dumps(
        data,
        indent=2,
        ensure_ascii=False,
        sort_keys=False,
    )


def is_empty(value: Any) -> bool:
    """
    Check whether a value is considered empty.

    Args:
        value: Value to inspect.

    Returns:
        True if empty, otherwise False.
    """
    if value is None:
        return True

    if isinstance(value, str):
        return not value.strip()

    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0

    return False


def truncate(text: str, max_length: int = 300) -> str:
    """
    Truncate long text while preserving readability.

    Args:
        text: Input text.
        max_length: Maximum output length.

    Returns:
        Truncated text.
    """
    text = text.strip()

    if len(text) <= max_length:
        return text

    return text[: max_length - 3].rstrip() + "..."