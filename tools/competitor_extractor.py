def extract_competitors(research_bundle: dict) -> str:
    try:
        results = research_bundle.get("serper", [])
        if not results:
            return "No competitor data available."

        competitors = []
        for item in results[:5]:
            title   = item.get("title", "No title")
            snippet = item.get("snippet", "No description")
            link    = item.get("link", "")
            competitors.append(f"- {title}\n  {snippet}\n  {link}")

        return "Competitor Intelligence:\n" + "\n\n".join(competitors)

    except Exception as e:
        return f"Error extracting competitors: {str(e)}"