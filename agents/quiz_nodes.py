from agents.quiz_agent import QuizAgent


def quiz_node(state):
    questions = QuizAgent.generate_quiz(
        subject=state["subject"],
        study_plan=state["study_plan"],
        difficulty=state["difficulty"],
        total_questions=state["total_questions"],
    )

    return {
        "questions": questions
    }