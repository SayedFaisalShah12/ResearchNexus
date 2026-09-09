from tools.tavily_search import web_research
from tools.web_scraper import scrape_webpage


def research_topic(query: str) -> dict:
    """
    Conduct web research for a given topic.

    The Research Agent:
    1. Searches the web using Tavily.
    2. Extracts URLs from the search results.
    3. Scrapes the webpages.
    4. Returns the collected research material.
    """

    search_output = web_research.invoke({
        "query": query
    })

    if not search_output:
        return {
            "query": query,
            "search_results": "",
            "documents": [],
        }

    # Extract URLs from Tavily's formatted output.
    urls = []

    for line in search_output.splitlines():
        if line.startswith("URL:"):
            url = line.replace("URL:", "", 1).strip()

            if url:
                urls.append(url)

    # Avoid scraping too many pages at this stage.
    urls = urls[:5]

    documents = []

    for url in urls:
        content = scrape_webpage.invoke({
            "url": url
        })

        documents.append({
            "url": url,
            "content": content,
        })

    return {
        "query": query,
        "search_results": search_output,
        "documents": documents,
    }