from agents.critic_agent import critique_report


if __name__ == "__main__":
    query = "latest developments in generative AI"

    research_material = """
    Generative AI has rapidly developed through advances in large language
    models, multimodal models, and AI agents.

    Modern generative AI systems can generate text, images, and code.

    AI agents extend generative AI by allowing models to use tools,
    perform multiple steps, and interact with external systems.
    """

    analysis = """
    Key findings:
    - Generative AI capabilities have expanded.
    - Multimodal systems can work with multiple forms of content.
    - AI agents extend generative AI through tool use and multi-step workflows.

    Important gap:
    - The provided research does not contain detailed quantitative
      comparisons between different models.
    """

    draft = """
    # Latest Developments in Generative AI

    ## Executive Summary

    Generative AI has advanced through improvements in large language
    models, multimodal systems, and AI agents.

    ## Key Findings

    Modern systems can generate text, images, and code.

    AI agents extend generative AI by allowing models to use tools
    and perform multi-step tasks.

    ## Detailed Analysis

    The development of multimodal systems and tool-using AI agents
    represents an important direction in generative AI.

    ## Conclusion

    Generative AI continues to develop through improvements in model
    capabilities and agentic workflows.
    """

    print("\n" + "=" * 60)
    print("CRITIC AGENT")
    print("=" * 60)

    critique = critique_report(
        query=query,
        research_material=research_material,
        analysis=analysis,
        draft=draft,
    )

    print("\n" + critique)