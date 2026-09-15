    from typing import TypedDict


class ResearchState(TypedDict, total=False):
    # User's research question
    query: str

    # Web research
    search_results: list
    urls: list
    documents: list

    # Analysis
    research_notes: str
    analysis: str

    # Report generation
    draft: str

    # Critic feedback
    critique: str

    # Revision control
    revision_count: int
    approved: bool

    # Final output
    final_report: str