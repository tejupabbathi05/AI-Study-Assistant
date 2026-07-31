from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from backend.config import llm


class TutorAgent:

    @staticmethod
    def answer_question(question: str) -> str:

        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert AI tutor. Explain concepts clearly in simple language with examples whenever helpful."
                ),
                (
                    "human",
                    "{question}"
                ),
            ]
        )

        chain = prompt | llm | StrOutputParser()

        return chain.invoke(
            {
                "question": question
            }
        )