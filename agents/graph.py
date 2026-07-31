from langgraph.graph import StateGraph, END

from backend.state import StudyState
from agents.nodes import planner_node


builder = StateGraph(StudyState)

builder.add_node(
    "planner",
    planner_node
)

builder.set_entry_point("planner")

builder.add_edge(
    "planner",
    END
)

study_graph = builder.compile()