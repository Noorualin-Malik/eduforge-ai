"""Evaluator agent for assessing the generated learning plan."""

from __future__ import annotations

from pathlib import Path

from state import EduForgeState
from tools.gemini import generate_json

PROMPT_PATH = Path("prompts/evaluator.md")


def _load_prompt() -> str:
    """Load the evaluator system prompt."""

    return PROMPT_PATH.read_text(encoding="utf-8")


def evaluator_node(state: EduForgeState) -> EduForgeState:
    """
    Evaluate the generated learning package.

    The evaluator reviews:
    - Learning roadmap
    - Research summary
    - Quiz quality

    It returns:
    - Overall score (1-10)
    - Completeness
    - Clarity
    - Learning progression
    - Strengths
    - Improvements
    """

    system_prompt = _load_prompt()

    user_prompt = f"""
Evaluate the following educational content.

Roadmap:
{state["roadmap"]}

Research:
{state["research"]}

Quiz:
{state["quiz"]}

Return ONLY valid JSON using this schema:

{{
  "overall_score": 0,
  "completeness": "",
  "clarity": "",
  "learning_progression": "",
  "strengths": [],
  "improvements": [],
  "feedback": ""
}}
"""

    evaluation = generate_json(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )

    state["evaluation"] = evaluation

    state["messages"].append(
        {
            "role": "assistant",
            "content": (
                f"Evaluation completed. "
                f'Score: {evaluation.get("overall_score", "N/A")}/10.'
            ),
        }
    )

    return state