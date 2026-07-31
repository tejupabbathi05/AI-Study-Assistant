from typing import TypedDict, List

from langgraph.graph import StateGraph, END

from agents.quiz_nodes import quiz_node


class QuizState(TypedDict, total=False):
    subject: str
    study_plan: str
    difficulty: str
    total_questions: int
    questions: List[dict]


builder = StateGraph(QuizState)

builder.add_node("generate_quiz", quiz_node)

builder.set_entry_point("generate_quiz")

builder.add_edge("generate_quiz", END)

quiz_graph = builder.compile()