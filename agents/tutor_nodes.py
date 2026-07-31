from agents.tutor_agents import TutorAgent


def tutor_node(state):

    answer = TutorAgent.answer_question(
        state["question"]
    )

    return {
        "answer": answer
    }