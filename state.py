"""Shared state definition for the EduForge LangGraph workflow."""

from __future__ import annotations

from typing import Any, Dict, List, TypedDict


class EduForgeState(TypedDict):
    """Shared state passed between all LangGraph agents."""

    # User input
    topic: str

    # Planner output
    roadmap: Dict[str, Any]

    # Researcher output
    research: Dict[str, Any]

    # Quiz output
    quiz: Dict[str, Any]

    # Evaluator output
    evaluation: Dict[str, Any]

    # Supervisor output
    final_output: Dict[str, Any]

    # Optional lightweight conversation history
    messages: List[Dict[str, str]]