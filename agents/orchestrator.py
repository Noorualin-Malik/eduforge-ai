"""Orchestrator agent for the EduForge workflow."""

from __future__ import annotations

from copy import deepcopy

from state import EduForgeState


def orchestrator_node(state: EduForgeState) -> EduForgeState:
    """
    Initialize and normalize the shared workflow state.

    This is the entry point of the LangGraph workflow. It ensures that all
    required fields exist before passing control to the Planner agent.
    """

    updated_state = deepcopy(state)

    updated_state.setdefault("topic", "")
    updated_state.setdefault("roadmap", {})
    updated_state.setdefault("research", {})
    updated_state.setdefault("quiz", {})
    updated_state.setdefault("evaluation", {})
    updated_state.setdefault("final_output", {})
    updated_state.setdefault("messages", [])

    topic = updated_state["topic"].strip()

    updated_state["messages"].append(
        {
            "role": "system",
            "content": f"Learning session initialized for topic: {topic}",
        }
    )

    return updated_state