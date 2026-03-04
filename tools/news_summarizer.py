def summarize_news(research_bundle: dict) -> str:
    try:
        articles = research_bundle.get("guardian", [])
        if not articles:
            return "No news articles available."

        summaries = []
        for i, article in enumerate(articles[:5]):
            title   = article.get("webTitle", "No title")
            date    = article.get("webPublicationDate", "Unknown date")
            section = article.get("sectionName", "Unknown section")
            summaries.append(f"{i+1}. [{date}] {title} (Section: {section})")

        return "Recent News:\n" + "\n".join(summaries)

    except Exception as e:
        return f"Error summarizing news: {str(e)}"