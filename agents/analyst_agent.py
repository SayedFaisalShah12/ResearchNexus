from chains.analysis_chain import create_analysis_chain


def analyze_research(query: str, research_material: str) -> str:
    """
    Analyze collected research material and produce structured insights.
    """

    chain = create_analysis_chain()

    response = chain.invoke(
        {
            "query": query,
            "research_material": research_material,
        }
    )

    return response