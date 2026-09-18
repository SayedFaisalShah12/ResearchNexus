from chains.writer_chain import create_writer_chain


def write_report(
    query: str,
    research_material: str,
    analysis: str,
) -> str:
    """
    Generate a professional research report from research and analysis.
    """

    chain = create_writer_chain()

    response = chain.invoke(
        {
            "query": query,
            "research_material": research_material,
            "analysis": analysis,
        }
    )

    return response