"""Supervisor agent for validating and assembling the final response."""

from __future__ import annotations

from copy import deepcopy

from state import EduForgeState


_REQUIRED_FIELDS = (
    "roadmap",
    "research",
    "quiz",
    "evaluation",
)


def _is_empty(value: object) -> bool:
    """Return True if a value should be considered empty."""

    if value is None:
        return True

    if isinstance(value, str):
        return not value.strip()

    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0

    return False


def _validate(state: EduForgeState) -> list[str]:
    """
    Validate that all required outputs exist.

    Returns:
        A list of validation errors. An empty list indicates success.
    """

    errors: list[str] = []

    for field in _REQUIRED_FIELDS:
        if field not in state:
            errors.append(f"Missing field: {field}")
            continue

        if _is_empty(state[field]):
            errors.append(f"Empty output: {field}")

    return errors


def supervisor_node(state: EduForgeState) -> EduForgeState:
    """
    Validate workflow outputs and prepare the final response.

    This agent performs lightweight validation only.
    """

    errors = _validate(state)

    final_output = {
        "topic": state["topic"],
        "roadmap": deepcopy(state["roadmap"]),
        "research": deepcopy(state["research"]),
        "quiz": deepcopy(state["quiz"]),
        "evaluation": deepcopy(state["evaluation"]),
        "validation": {
            "passed": len(errors) == 0,
            "errors": errors,
        },
    }

    state["final_output"] = final_output

    state["messages"].append(
        {
            "role": "assistant",
            "content": (
                "Supervisor validation passed."
                if not errors
                else "Supervisor detected validation issues."
            ),
        }
    )

    return state