from agents.analyst_agent import analyze_research


if __name__ == "__main__":
    query = "latest developments in generative AI"

    research_material = """
    Generative AI has rapidly developed through advances in large language
    models, multimodal models, and AI agents. Modern systems can generate
    text, images, code, and other forms of content.

    AI agents extend generative AI by allowing models to use tools, perform
    multiple steps, and interact with external systems.
    """

    print("\n" + "=" * 60)
    print("ANALYST AGENT")
    print("=" * 60)

    analysis = analyze_research(query, research_material)

    print("\n" + analysis)