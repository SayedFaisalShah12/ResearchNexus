from workflows.graph import build_research_graph


if __name__ == "__main__":
    graph = build_research_graph()

    initial_state = {
        "query": "latest developments in generative AI",
        "revision_count": 0,
        "approved": False,
    }

    print("\n" + "=" * 60)
    print("RESEARCHNEXUS LANGGRAPH WORKFLOW")
    print("=" * 60)

    final_state = graph.invoke(initial_state)

    print("\n" + "=" * 60)
    print("WORKFLOW COMPLETED")
    print("=" * 60)

    print("\nAnalysis:")
    print(final_state.get("analysis", ""))

    print("\nDraft:")
    print(final_state.get("draft", ""))

    print("\nCritique:")
    print(final_state.get("critique", ""))