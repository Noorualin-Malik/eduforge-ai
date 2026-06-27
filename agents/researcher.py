"""Researcher agent for collecting and summarizing learning resources."""

from __future__ import annotations

from pathlib import Path

from state import EduForgeState
from tools.gemini import generate_json
from tools.search import search_resources

PROMPT_PATH = Path("prompts/researcher.md")


def _load_prompt() -> str:
    """Load the researcher system prompt."""

    return PROMPT_PATH.read_text(encoding="utf-8")


def researcher_node(state: EduForgeState) -> EduForgeState:
    """
    Collect learning resources using Tavily and summarize them with Gemini.
    """

    topic = state["topic"]

    resources = search_resources(topic)

    system_prompt = _load_prompt()

    user_prompt = f"""
Topic:
{topic}

Search Results:

{resources}

Summarize these resources into concise study notes.

Return ONLY valid JSON using this schema:

{{
  "summary": "",
  "key_concepts": [],
  "recommended_articles": [],
  "documentation": [],
  "tutorials": [],
  "github_repositories": [],
  "study_tips": []
}}
"""

    research = generate_json(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )

    state["research"] = {
        "sources": resources,
        "summary": research,
    }

    state["messages"].append(
        {
            "role": "assistant",
            "content": "Research resources collected and summarized.",
        }
    )

    return state