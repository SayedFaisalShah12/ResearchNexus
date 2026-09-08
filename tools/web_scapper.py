import requests
from bs4 import BeautifulSoup
from langchain_core.tools import tool


@tool
def scrape_webpage(url: str) -> str:
    """
    Fetch and extract readable text from a webpage.

    Args:
        url: The URL of the webpage to scrape.

    Returns:
        Cleaned webpage text.
    """

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15,
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove elements that don't contain useful article content
        for element in soup(
            ["script", "style", "nav", "footer", "header", "aside"]
        ):
            element.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True,
        )

        # Prevent extremely large pages from overwhelming the LLM
        max_chars = 12000

        if len(text) > max_chars:
            text = text[:max_chars] + "\n[Content truncated]"

        return text

    except requests.RequestException as exc:
        return f"Failed to fetch webpage: {exc}"

    except Exception as exc:
        return f"Failed to process webpage: {exc}"