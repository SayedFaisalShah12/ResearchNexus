from chains.critic_chain import create_critic_chain


def critique_report(
    query: str,
    research_material: str,
    analysis: str,
    draft: str,
) -> str:
    """
    Evaluate a research report draft against the research material
    and analyst's findings.
    """

    chain = create_critic_chain()

    response = chain.invoke(
        {
            "query": query,
            "research_material": research_material,
            "analysis": analysis,
            "draft": draft,
        }
    )

    return response