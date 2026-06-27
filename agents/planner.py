"""Planner agent for generating a structured learning roadmap."""

from __future__ import annotations

from pathlib import Path

from state import EduForgeState
from tools.gemini import generate_json


PROMPT_PATH = Path("prompts/planner.md")


def _load_prompt() -> str:
    """Load the planner system prompt."""

    return PROMPT_PATH.read_text(encoding="utf-8")


def planner_node(state: EduForgeState) -> EduForgeState:
    """
    Generate a personalized learning roadmap.

    The planner creates:
    - Learning objectives
    - Weekly study plan
    - Estimated duration
    - Recommended prerequisites
    - Suggested projects
    """

    topic = state["topic"]

    system_prompt = _load_prompt()

    user_prompt = f"""
Topic:
{topic}

Create a complete learning roadmap.

Return ONLY valid JSON with the following schema:

{{
  "title": "",
  "difficulty": "",
  "estimated_duration": "",
  "learning_objectives": [],
  "prerequisites": [],
  "weekly_plan": [
    {{
      "week": 1,
      "topics": [],
      "goals": []
    }}
  ],
  "recommended_projects": []
}}
"""

    roadmap = generate_json(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )

    state["roadmap"] = roadmap

    state["messages"].append(
        {
            "role": "assistant",
            "content": "Learning roadmap generated successfully.",
        }
    )

    return state