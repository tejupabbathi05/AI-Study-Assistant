from typing import TypedDict


class StudyState(TypedDict):
    subject: str
    exam_date: str
    hours_per_day: int
    goal: str
    study_plan: str