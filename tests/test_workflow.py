from workflows.graph import build_research_graph


if __name__ == "__main__":
    graph = build_research_graph()

    initial_state = {
        "query": "latest developments in generative AI",
        "revision_count": 0,
        "approved": False,
    }

    print("\n" + "=" * 70)
    print("RESEARCHNEXUS MULTI-AGENT WORKFLOW")
    print("=" * 70)

    final_state = graph.invoke(initial_state)

    print("\n" + "=" * 70)
    print("WORKFLOW COMPLETED")
    print("=" * 70)

    print("\nApproved:")
    print(final_state.get("approved", False))

    print("\nRevision Count:")
    print(final_state.get("revision_count", 0))

    print("\n" + "-" * 70)
    print("FINAL REPORT")
    print("-" * 70)

    print(final_state.get("final_report", ""))

    print("\n" + "-" * 70)
    print("FINAL CRITIQUE")
    print("-" * 70)

    print(final_state.get("critique", ""))

    print("\n" + "=" * 70)
    print("END OF RESEARCHNEXUS WORKFLOW")
    print("=" * 70)