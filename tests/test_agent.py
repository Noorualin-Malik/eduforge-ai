"""Basic tests for the EduForge agent workflow."""

from __future__ import annotations

from agents.orchestrator import orchestrator_node
from agents.planner import planner_node
from agents.researcher import researcher_node
from agents.quiz import quiz_node
from agents.evaluator import evaluator_node
from agents.supervisor import supervisor_node


def initial_state() -> dict:
    """Create a valid initial workflow state."""

    return {
        "topic": "Python",
        "roadmap": {},
        "research": {},
        "quiz": {},
        "evaluation": {},
        "final_output": {},
        "messages": [],
    }


def test_orchestrator_initializes_state():
    """The orchestrator should initialize the workflow state."""

    state = orchestrator_node(initial_state())

    assert state["topic"] == "Python"
    assert isinstance(state["messages"], list)
    assert len(state["messages"]) > 0


def test_complete_workflow():
    """
    Execute the complete workflow.

    These tests require valid GOOGLE_API_KEY and
    TAVILY_API_KEY environment variables.
    """

    state = initial_state()

    state = orchestrator_node(state)
    state = planner_node(state)
    state = researcher_node(state)
    state = quiz_node(state)
    state = evaluator_node(state)
    state = supervisor_node(state)

    assert state["roadmap"]
    assert state["research"]
    assert state["quiz"]
    assert state["evaluation"]
    assert state["final_output"]

    validation = state["final_output"]["validation"]

    assert validation["passed"] is True
    assert validation["errors"] == []


def test_final_output_contains_all_sections():
    """Supervisor output should include every required section."""

    state = initial_state()

    state = orchestrator_node(state)
    state = planner_node(state)
    state = researcher_node(state)
    state = quiz_node(state)
    state = evaluator_node(state)
    state = supervisor_node(state)

    final = state["final_output"]

    assert "topic" in final
    assert "roadmap" in final
    assert "research" in final
    assert "quiz" in final
    assert "evaluation" in final
    assert "validation" in final


def test_validation_schema():
    """Validation object should follow the expected schema."""

    state = initial_state()

    state = orchestrator_node(state)
    state = planner_node(state)
    state = researcher_node(state)
    state = quiz_node(state)
    state = evaluator_node(state)
    state = supervisor_node(state)

    validation = state["final_output"]["validation"]

    assert isinstance(validation["passed"], bool)
    assert isinstance(validation["errors"], list)