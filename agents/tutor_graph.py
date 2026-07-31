from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.tutor_nodes import tutor_node


class TutorState(TypedDict):
    question: str
    answer: str


builder = StateGraph(TutorState)

builder.add_node(
    "tutor",
    tutor_node
)

builder.set_entry_point(
    "tutor"
)

builder.add_edge(
    "tutor",
    END
)

tutor_graph = builder.compile()