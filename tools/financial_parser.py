def parse_financials(research_bundle: dict) -> str:
    try:
        data = research_bundle.get("alphavantage", {})
        if not data:
            return "No financial data available."

        overview = data.get("overview", {})
        name     = overview.get("Name", "Unknown")
        symbol   = overview.get("Symbol", "N/A")
        market   = overview.get("MarketCapitalization", "N/A")
        pe       = overview.get("PERatio", "N/A")
        revenue  = overview.get("RevenueTTM", "N/A")
        sector   = overview.get("Sector", "N/A")

        return f"""
Company: {name} ({symbol})
Sector: {sector}
Market Cap: {market}
P/E Ratio: {pe}
Revenue (TTM): {revenue}
""".strip()

    except Exception as e:
        return f"Error parsing financials: {str(e)}"