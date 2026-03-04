# tools/mcp_registry.py
from langchain.tools import tool
from tools.financial_parser import parse_financials
from tools.news_summarizer import summarize_news
from tools.competitor_extractor import extract_competitors

@tool
def financial_parser(research_bundle: dict) -> str:
    """Parses Alpha Vantage financial data for a company."""
    return parse_financials(research_bundle)

@tool
def news_summarizer(research_bundle: dict) -> str:
    """Summarizes Guardian news articles about a company."""
    return summarize_news(research_bundle)

@tool
def competitor_extractor(research_bundle: dict) -> str:
    """Extracts competitor mentions from Serper search results."""
    return extract_competitors(research_bundle)

# This is the list we pass to the ReAct agent
TOOLS = [financial_parser, news_summarizer, competitor_extractor]