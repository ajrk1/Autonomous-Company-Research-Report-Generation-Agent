# INTEL.ai — Autonomous Company Research Agent

> Enter a company name + ticker. The agent does everything else.

## What It Does
An AI-powered pipeline that autonomously generates comprehensive strategic intelligence reports using real-time data from multiple APIs.

## Features
- Company name + ticker symbol input
- Real-time data from Serper, Guardian, and Alpha Vantage APIs
- LangGraph ReAct agent with 6 nodes and validation/retry logic
- Pinecone RAG for structural guidance
- Professional dark-themed web interface (INTEL.ai)
- PDF export with dark theme preserved
- Public URL via ngrok

## Tech Stack
| Component | Technology |
|-----------|-----------|
| Orchestration | n8n |
| Agent Framework | LangGraph |
| Language Model | GPT-4o-mini |
| Vector Database | Pinecone |
| Web Search | Serper API |
| News | Guardian API |
| Financials | Alpha Vantage |
| Backend | Flask (Python) |
| Tunnel | Cloudflare + ngrok |

## Setup
1. Clone the repo
2. Create `.env` with your API keys:
```
OPENAI_API_KEY=
PINECONE_API_KEY=
SERPER_API_KEY=
GUARDIAN_API_KEY=
ALPHA_VANTAGE_API_KEY=
```
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python agent/server.py`
5. Open: `http://127.0.0.1:5000`

## Team
Ironhack AI Bootcamp — Group 01 — March 2026
