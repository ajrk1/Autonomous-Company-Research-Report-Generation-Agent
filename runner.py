import json
import sys
import os
from datetime import datetime
from agent.graph import build_graph

os.makedirs("logs", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

input_data = json.loads(sys.argv[1])
company = input_data["company"].replace(" ", "_")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

graph = build_graph()
result = graph.invoke({
    "company_name": input_data["company"],
    "research_bundle": input_data.get("research_bundle", {}),
    "retrieved_guidance": [],
    "react_findings": {},
    "draft_report": "",
    "validation_flag": False,
    "retry_count": 0,
    "logs": [],
    "errors": []
})

report_path = f"outputs/{company}_{timestamp}.md"
with open(report_path, "w") as f:
    f.write(result["draft_report"])

log_path = f"logs/{company}_{timestamp}.log"
with open(log_path, "w") as f:
    f.write("\n".join(result["logs"]))

print(json.dumps({
    "status": "done",
    "report_path": report_path,
    "errors": result["errors"]
}))