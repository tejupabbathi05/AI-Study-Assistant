from datetime import date

from langchain_core.prompts import ChatPromptTemplate

from backend.config import llm


class PlannerAgent:

    @staticmethod
    def generate_plan(subject, exam_date, hours_per_day, goal):

        today = date.today()

        days_left = (exam_date - today).days

        if days_left < 0:
            days_left = 0

        prompt = ChatPromptTemplate.from_template(
            """
You are an expert AI Study Planner.

Today's Date:
{today}

Exam Date:
{exam_date}

Days Remaining:
{days_left}

Subject:
{subject}

Available Study Hours Per Day:
{hours_per_day}

Goal:
{goal}

Instructions:

- NEVER assume a different exam date.
- NEVER create a yearly or monthly roadmap if the exam is near.
- Use the exact number of days remaining.
- If Days Remaining is 0, create a ONE-DAY crash revision plan.
- If Days Remaining is 1-7, create a daily revision schedule.
- If Days Remaining is 8-30, create a weekly + daily schedule.
- If Days Remaining is more than 30, create a long-term study plan.
- Mention the number of days remaining in the overview.

Return the response in Markdown.

# Study Plan

## Overview

## Schedule

## Topics

## Revision Strategy

## Tips
"""
        )

        chain = prompt | llm

        response = chain.invoke(
            {
                "today": today,
                "exam_date": exam_date,
                "days_left": days_left,
                "subject": subject,
                "hours_per_day": hours_per_day,
                "goal": goal,
            }
        )

        return response.content