from agents.research_agent import research_topic
from agents.analyst_agent import analyze_research
from agents.writer_agent import write_report
from agents.critic_agent import critique_report
from schemas.state import ResearchState


def research_node(state: ResearchState) -> dict:
    """Run the Research Agent and update the shared state."""

    query = state["query"]

    result = research_topic(query)

    return {
        "search_results": result.get("search_results", ""),
        "documents": result.get("documents", []),
    }


def analyst_node(state: ResearchState) -> dict:
    """Run the Analyst Agent using the collected research."""

    query = state["query"]
    documents = state.get("documents", [])

    research_material = "\n\n".join(
        f"URL: {document.get('url', '')}\n"
        f"CONTENT:\n{document.get('content', '')}"
        for document in documents
    )

    analysis = analyze_research(
        query=query,
        research_material=research_material,
    )

    return {
        "analysis": analysis,
    }


def writer_node(state: ResearchState) -> dict:
    """Run the Writer Agent using research and analysis."""

    query = state["query"]
    documents = state.get("documents", [])
    analysis = state.get("analysis", "")

    research_material = "\n\n".join(
        f"URL: {document.get('url', '')}\n"
        f"CONTENT:\n{document.get('content', '')}"
        for document in documents
    )

    draft = write_report(
        query=query,
        research_material=research_material,
        analysis=analysis,
    )

    return {
        "draft": draft,
    }


def critic_node(state: ResearchState) -> dict:
    """Run the Critic Agent against the current draft."""

    query = state["query"]
    documents = state.get("documents", [])
    analysis = state.get("analysis", "")
    draft = state.get("draft", "")

    research_material = "\n\n".join(
        f"URL: {document.get('url', '')}\n"
        f"CONTENT:\n{document.get('content', '')}"
        for document in documents
    )

    critique = critique_report(
        query=query,
        research_material=research_material,
        analysis=analysis,
        draft=draft,
    )

    return {
        "critique": critique,
    }