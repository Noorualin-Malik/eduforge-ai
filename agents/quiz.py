"""Quiz agent for generating assessment questions."""

from __future__ import annotations

from pathlib import Path

from state import EduForgeState
from tools.gemini import generate_json

PROMPT_PATH = Path("prompts/quiz.md")


def _load_prompt() -> str:
    """Load the quiz system prompt."""
    return PROMPT_PATH.read_text(encoding="utf-8")


def quiz_node(state: EduForgeState) -> EduForgeState:
    """
    Generate a quiz based on the learning roadmap.

    The quiz contains:
    - Multiple-choice questions
    - Short-answer questions
    - Correct answers
    - Explanations
    """

    topic = state["topic"]
    roadmap = state["roadmap"]

    system_prompt = _load_prompt()

    user_prompt = f"""
Topic:
{topic}

Learning Roadmap:
{roadmap}

Generate a quiz that aligns with the roadmap.

Return ONLY valid JSON using this schema:

{{
  "mcqs": [
    {{
      "question": "",
      "options": [
        "",
        "",
        "",
        ""
      ],
      "answer": "",
      "explanation": ""
    }}
  ],
  "short_answer": [
    {{
      "question": "",
      "answer": "",
      "explanation": ""
    }}
  ]
}}
"""

    quiz = generate_json(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )

    state["quiz"] = quiz

    state["messages"].append(
        {
            "role": "assistant",
            "content": "Quiz generated successfully.",
        }
    )

    return state