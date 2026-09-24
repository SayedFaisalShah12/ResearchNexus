from chains.writer_chain import create_writer_chain


def write_report(
    query: str,
    research_material: str,
    analysis: str,
    previous_draft: str = "",
    critique: str = "",
) -> str:
    """
    Generate a new research report or revise an existing draft.
    """

    chain = create_writer_chain()

    response = chain.invoke(
        {
            "query": query,
            "research_material": research_material,
            "analysis": analysis,
            "previous_draft": previous_draft,
            "critique": critique,
        }
    )

    return response