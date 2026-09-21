from langgraph.graph import END, START, StateGraph

from schemas.state import ResearchState
from workflows.nodes import (
    analyst_node,
    critic_node,
    research_node,
    writer_node,
)


def build_research_graph():
    """Build the ResearchNexus LangGraph workflow."""

    graph = StateGraph(ResearchState)

    # Register nodes
    graph.add_node("research", research_node)
    graph.add_node("analysis", analyst_node)
    graph.add_node("writer", writer_node)
    graph.add_node("critic", critic_node)

    # Define workflow order
    graph.add_edge(START, "research")
    graph.add_edge("research", "analysis")
    graph.add_edge("analysis", "writer")
    graph.add_edge("writer", "critic")
    graph.add_edge("critic", END)

    return graph.compile()