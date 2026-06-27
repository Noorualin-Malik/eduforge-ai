"""Tavily Search integration for EduForge."""

from __future__ import annotations

from typing import Any

from tavily import TavilyClient

from config import settings


_client: TavilyClient | None = None


def get_client() -> TavilyClient:
    """
    Return a shared Tavily client instance.
    """

    global _client

    if _client is None:
        settings.validate()
        _client = TavilyClient(api_key=settings.tavily_api_key)

    return _client


def _categorize(url: str) -> str:
    """
    Categorize a resource based on its URL.
    """

    url = url.lower()

    if "github.com" in url:
        return "github"

    if "docs." in url or "documentation" in url:
        return "documentation"

    if any(site in url for site in ("youtube.com", "youtu.be")):
        return "tutorial"

    if any(site in url for site in ("medium.com", "dev.to")):
        return "article"

    return "resource"


def search_resources(
    topic: str,
    max_results: int = 8,
) -> dict[str, Any]:
    """
    Search the web for high-quality learning resources.

    Args:
        topic:
            Learning topic.

        max_results:
            Maximum number of search results.

    Returns:
        Structured search results.
    """

    client = get_client()

    response = client.search(
        query=f"{topic} learning resources documentation tutorial GitHub",
        search_depth="advanced",
        max_results=max_results,
        include_answer=True,
        include_raw_content=False,
    )

    resources = {
        "answer": response.get("answer", ""),
        "articles": [],
        "documentation": [],
        "tutorials": [],
        "github_repositories": [],
        "other_resources": [],
    }

    for item in response.get("results", []):

        result = {
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", ""),
        }

        category = _categorize(result["url"])

        if category == "article":
            resources["articles"].append(result)

        elif category == "documentation":
            resources["documentation"].append(result)

        elif category == "tutorial":
            resources["tutorials"].append(result)

        elif category == "github":
            resources["github_repositories"].append(result)

        else:
            resources["other_resources"].append(result)

    return resources