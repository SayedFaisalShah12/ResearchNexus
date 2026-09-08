import os

from dotenv import load_dotenv
from tavily import TavilyClient
from langchain_core.tools import tool


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is not set in the environment.")

tavily_client = TavilyClient(api_key=TAVILY_API_KEY)


@tool
def web_research(query: str) -> str:
    """
    Search the web for relevant information about a research topic.

    Returns titles, URLs, and content snippets from the search results.
    """

    response = tavily_client.search(
        query=query,
        max_results=5,
    )

    results = response.get("results", [])

    if not results:
        return "No relevant search results were found."

    formatted_results = []

    for index, result in enumerate(results, start=1):
        title = result.get("title", "Untitled")
        url = result.get("url", "")
        content = result.get("content", "")

        formatted_results.append(
            f"""
Result {index}
Title: {title}
URL: {url}
Content: {content}
"""
        )

    return "\n".join(formatted_results)