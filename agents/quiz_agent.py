import json

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from backend.config import llm


class QuizAgent:

    @staticmethod
    def generate_quiz(
        subject: str,
        study_plan: str,
        difficulty: str,
        total_questions: int,
    ):
        prompt = ChatPromptTemplate.from_template(
            """
You are an expert quiz generator.

Generate {total_questions} {difficulty} multiple-choice questions for the subject "{subject}".

Use this study plan as the syllabus:

{study_plan}

Return ONLY a valid JSON array.

Each object must follow this format:

[
  {{
    "question":"...",
    "option_a":"...",
    "option_b":"...",
    "option_c":"...",
    "option_d":"...",
    "correct_answer":"A",
    "explanation":"..."
  }}
]

Rules:
- No markdown
- No ```json
- Return ONLY JSON
- correct_answer must be A, B, C or D
"""
        )

        chain = prompt | llm | StrOutputParser()

        response = chain.invoke(
            {
                "subject": subject,
                "study_plan": study_plan,
                "difficulty": difficulty,
                "total_questions": total_questions,
            }
        )

        return json.loads(response)