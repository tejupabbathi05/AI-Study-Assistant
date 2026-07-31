from agents.planner_agent import PlannerAgent


def planner_node(state):

    subject = state["subject"]
    exam_date = state["exam_date"]
    hours_per_day = state["hours_per_day"]
    goal = state["goal"]

    study_plan = PlannerAgent.generate_plan(
        subject=subject,
        exam_date=exam_date,
        hours_per_day=hours_per_day,
        goal=goal,
    )

    state["study_plan"] = study_plan

    return state