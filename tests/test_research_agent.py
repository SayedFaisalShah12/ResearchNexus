from agents.research_agent import research_topic


if __name__ == "__main__":
    query = "latest developments in generative AI"

    result = research_topic(query)

    print("\n" + "=" * 60)
    print("RESEARCH QUERY")
    print("=" * 60)
    print(result["query"])

    print("\n" + "=" * 60)
    print("SEARCH RESULTS")
    print("=" * 60)
    print(result["search_results"])

    print("\n" + "=" * 60)
    print("SCRAPED DOCUMENTS")
    print("=" * 60)

    for index, document in enumerate(result["documents"], start=1):
        print(f"\n--- Document {index} ---")
        print("URL:", document["url"])
        print("Content preview:")
        print(document["content"][:1000])