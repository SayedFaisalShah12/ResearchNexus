from agents.research_agent import research_topic
from agents.analyst_agent import analyze_research
from agents.writer_agent import write_report
from agents.critic_agent import critique_report
from schemas.state import ResearchState


def research_node(state: ResearchState) -> dict:
    """
    Run the Research Agent and collect web research.
    """

    print("\n[1/5] Research Agent: searching the web...")

    query = state["query"]

    result = research_topic(query)

    documents = result.get("documents", [])

    print(
        f"Research Agent: collected {len(documents)} documents."
    )

    return {
        "search_results": result.get("search_results", ""),
        "documents": documents,
    }


def analyst_node(state: ResearchState) -> dict:
    """
    Run the Analyst Agent on the collected research.
    """

    print("\n[2/5] Analyst Agent: analyzing research...")

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

    print("Analyst Agent: analysis completed.")

    return {
        "analysis": analysis,
    }


def writer_node(state: ResearchState) -> dict:
    """
    Run the Writer Agent to create or revise a research report.
    """

    print("\n[3/5] Writer Agent: generating/revising report...")

    query = state["query"]
    documents = state.get("documents", [])
    analysis = state.get("analysis", "")

    # If this is a revision cycle, these contain
    # the previous draft and critic feedback.
    previous_draft = state.get("draft", "")
    critique = state.get("critique", "")

    research_material = "\n\n".join(
        f"URL: {document.get('url', '')}\n"
        f"CONTENT:\n{document.get('content', '')}"
        for document in documents
    )

    draft = write_report(
        query=query,
        research_material=research_material,
        analysis=analysis,
        previous_draft=previous_draft,
        critique=critique,
    )

    if previous_draft:
        print("Writer Agent: report revised.")
    else:
        print("Writer Agent: initial report generated.")

    return {
        "draft": draft,
    }


def critic_node(state: ResearchState) -> dict:
    """
    Run the Critic Agent to evaluate the current report draft.
    """

    print("\n[4/5] Critic Agent: evaluating report...")

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

    print("Critic Agent: evaluation completed.")

    return {
        "critique": critique,
    }


def decision_node(state: ResearchState) -> dict:
    """
    Decide whether the draft is approved or requires revision.

    The workflow allows a maximum of two revision cycles.
    """

    print("\n[5/5] Decision Node: evaluating critic verdict...")

    critique = state.get("critique", "")
    revision_count = state.get("revision_count", 0)

    max_revisions = 2

    # ---------------------------------------------------------
    # Extract the critic verdict
    # ---------------------------------------------------------

    critique_upper = critique.upper()

    if "VERDICT:" in critique_upper:
        verdict_section = critique_upper.split("VERDICT:", 1)[1]

        # Only inspect the text immediately following VERDICT.
        verdict = verdict_section.split("\n", 1)[0].strip()
    else:
        verdict = ""

    # ---------------------------------------------------------
    # APPROVED
    # ---------------------------------------------------------

    if verdict.startswith("APPROVED"):
        print("Decision: APPROVED")
        print("Final report is ready.")

        return {
            "approved": True,
            "final_report": state.get("draft", ""),
        }

    # ---------------------------------------------------------
    # MAXIMUM REVISION LIMIT
    # ---------------------------------------------------------

    if revision_count >= max_revisions:
        print("Decision: maximum revisions reached.")
        print("Using the current draft as the final report.")

        return {
            "approved": True,
            "final_report": state.get("draft", ""),
        }

    # ---------------------------------------------------------
    # REVISION REQUIRED
    # ---------------------------------------------------------

    next_revision = revision_count + 1

    print(
        f"Decision: REVISION_REQUIRED "
        f"(revision {next_revision}/{max_revisions})"
    )

    return {
        "approved": False,
        "revision_count": next_revision,
    }
    """
    Decide whether the draft is approved or requires revision.

    The workflow allows a maximum of two revision cycles.
    """

    print("\n[5/5] Decision Node: evaluating critic verdict...")

    critique = state.get("critique", "")
    revision_count = state.get("revision_count", 0)

    max_revisions = 2

    # ---------------------------------------------------------
    # APPROVAL
    # ---------------------------------------------------------

    if "APPROVED" in critique.upper():
        print("Decision: APPROVED")
        print("Final report is ready.")

        return {
            "approved": True,
            "final_report": state.get("draft", ""),
        }

    # ---------------------------------------------------------
    # MAXIMUM REVISION LIMIT
    # ---------------------------------------------------------

    if revision_count >= max_revisions:
        print("Decision: maximum revisions reached.")
        print("Using the current draft as the final report.")

        return {
            "approved": True,
            "final_report": state.get("draft", ""),
        }

    # ---------------------------------------------------------
    # REVISION REQUIRED
    # ---------------------------------------------------------

    next_revision = revision_count + 1

    print(
        f"Decision: REVISION_REQUIRED "
        f"(revision {next_revision}/{max_revisions})"
    )

    return {
        "approved": False,
        "revision_count": next_revision,
    }