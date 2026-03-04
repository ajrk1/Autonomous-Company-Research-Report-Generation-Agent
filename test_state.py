# test_state.py
from agent.state import ResearchState

# Create a dummy state to verify everything works
test_state: ResearchState = {
    "company_name": "Apple",
    "research_bundle": {"serper": [], "guardian": [], "alphavantage": {}},
    "retrieved_guidance": [],
    "react_findings": {},
    "draft_report": "",
    "validation_flag": False,
    "retry_count": 0,
    "logs": [],
    "errors": []
}

print("✅ ResearchState imported successfully!")
print(f"Company: {test_state['company_name']}")
print(f"Validation flag: {test_state['validation_flag']}")
print(f"Retry count: {test_state['retry_count']}")