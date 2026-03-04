from langgraph.graph import StateGraph, END
from agent.state import ResearchState
from agent.nodes import research_node, rag_node, synthesis_node, report_node, validation_node

def should_retry(state):
    if not state.get("validation_flag") and state.get("retry_count", 0) < 1:
        return "retry"
    return "end"

def build_graph():
    graph = StateGraph(ResearchState)
    graph.add_node("research", research_node)
    graph.add_node("rag", rag_node)
    graph.add_node("synthesis", synthesis_node)
    graph.add_node("report", report_node)
    graph.add_node("validation", validation_node)
    graph.set_entry_point("research")
    graph.add_edge("research", "rag")
    graph.add_edge("rag", "synthesis")
    graph.add_edge("synthesis", "report")
    graph.add_edge("report", "validation")
    graph.add_conditional_edges("validation", should_retry, {
        "retry": "research",
        "end": END
    })
    return graph.compile()