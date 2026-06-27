"""LangGraph workflow definition for EduForge."""

from __future__ import annotations

from langgraph.graph import END, StateGraph

from agents.evaluator import evaluator_node
from agents.orchestrator import orchestrator_node
from agents.planner import planner_node
from agents.quiz import quiz_node
from agents.researcher import researcher_node
from agents.supervisor import supervisor_node
from state import EduForgeState


def build_graph():
    """Build and compile the EduForge workflow."""

    workflow = StateGraph(EduForgeState)

    workflow.add_node("orchestrator", orchestrator_node)
    workflow.add_node("planner", planner_node)
    workflow.add_node("researcher", researcher_node)
    workflow.add_node("quiz", quiz_node)
    workflow.add_node("evaluator", evaluator_node)
    workflow.add_node("supervisor", supervisor_node)

    workflow.set_entry_point("orchestrator")

    workflow.add_edge("orchestrator", "planner")
    workflow.add_edge("planner", "researcher")
    workflow.add_edge("researcher", "quiz")
    workflow.add_edge("quiz", "evaluator")
    workflow.add_edge("evaluator", "supervisor")
    workflow.add_edge("supervisor", END)

    return workflow.compile()