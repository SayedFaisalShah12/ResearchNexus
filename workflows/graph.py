from langgraph.graph import END, START, StateGraph

from schemas.state import ResearchState
from workflows.nodes import (
    analyst_node,
    critic_node,
    decision_node,
    research_node,
    writer_node,
)


def route_after_critic(state: ResearchState) -> str:
    """
    Route the workflow based on the critic's decision.
    """

    if state.get("approved", False):
        return "final"

    return "revision"


def build_research_graph():
    """Build the ResearchNexus LangGraph workflow."""

    graph = StateGraph(ResearchState)

    graph.add_node("research", research_node)
    graph.add_node("analysis", analyst_node)
    graph.add_node("writer", writer_node)
    graph.add_node("critic", critic_node)
    graph.add_node("decision", decision_node)

    graph.add_edge(START, "research")
    graph.add_edge("research", "analysis")
    graph.add_edge("analysis", "writer")
    graph.add_edge("writer", "critic")
    graph.add_edge("critic", "decision")

    graph.add_conditional_edges(
        "decision",
        route_after_critic,
        {
            "final": END,
            "revision": "writer",
        },
    )

    return graph.compile()