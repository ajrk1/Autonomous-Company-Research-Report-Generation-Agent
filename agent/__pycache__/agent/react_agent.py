# agent/react_agent.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools.mcp_registry import TOOLS

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

react_agent = create_react_agent(llm, TOOLS)