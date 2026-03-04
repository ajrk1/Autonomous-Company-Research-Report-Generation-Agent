from typing import TypedDict, List, Dict, Any

class ResearchState(TypedDict):
    company_name:       str
    research_bundle:    Dict[str, Any]
    retrieved_guidance: List[str]
    react_findings:     Dict[str, Any]
    draft_report:       str
    validation_flag:    bool
    retry_count:        int
    logs:               List[str]
    errors:             List[str]
