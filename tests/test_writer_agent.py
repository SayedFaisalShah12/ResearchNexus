from agents.writer_agent import write_report


if __name__ == "__main__":
    query = "latest developments in generative AI"

    research_material = """
    Generative AI has rapidly developed through advances in large language
    models, multimodal models, and AI agents. Modern systems can generate
    text, images, code, and other forms of content.

    AI agents extend generative AI by allowing models to use tools, perform
    multiple steps, and interact with external systems.
    """

    analysis = """
    Key findings:
    - Generative AI capabilities have expanded significantly.
    - Multimodal models can process and generate multiple forms of content.
    - AI agents extend generative AI through tool use and multi-step workflows.

    Main themes:
    - Increasing model capabilities
    - Multimodal AI
    - Tool-using AI agents

    Important gaps:
    - The provided material does not contain detailed quantitative comparisons.
    """

    print("\n" + "=" * 60)
    print("WRITER AGENT")
    print("=" * 60)

    report = write_report(
        query=query,
        research_material=research_material,
        analysis=analysis,
    )

    print("\n" + report)