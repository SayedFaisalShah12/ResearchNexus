from schemas.state import ResearchState


def test_research_state():
    state: ResearchState = {
        "query": "latest developments in generative AI",
        "search_results": [],
        "urls": [],
        "documents": [],
        "analysis": "",
        "draft": "",
        "critique": "",
        "revision_count": 0,
        "approved": False,
        "final_report": "",
    }

    assert state["query"] == "latest developments in generative AI"
    assert state["revision_count"] == 0
    assert state["approved"] is False

    print("ResearchState test: OK")


if __name__ == "__main__":
    test_research_state()