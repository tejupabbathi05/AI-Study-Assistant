from sqlalchemy.orm import Session

from backend.models import (
    Quiz,
    QuizQuestion,
    QuizAttempt,
    StudySession,
)


class QuizService:

    @staticmethod
    def get_study_plans(db: Session, user_id: int):
        return (
            db.query(StudySession)
            .filter(StudySession.user_id == user_id)
            .order_by(StudySession.created_at.desc())
            .all()
        )

    @staticmethod
    def create_quiz(
        db: Session,
        study_session_id: int,
        difficulty: str,
        questions_data: list,
    ):
        quiz = Quiz(
            study_session_id=study_session_id,
            difficulty=difficulty,
            total_questions=len(questions_data),
        )

        db.add(quiz)
        db.commit()
        db.refresh(quiz)

        for q in questions_data:
            question = QuizQuestion(
                quiz_id=quiz.id,
                question=q["question"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_answer=q["correct_answer"],
                explanation=q.get("explanation", ""),
            )
            db.add(question)

        db.commit()

        return quiz

    @staticmethod
    def get_quiz(db: Session, quiz_id: int):
        return (
            db.query(Quiz)
            .filter(Quiz.id == quiz_id)
            .first()
        )

    @staticmethod
    def get_quiz_questions(db: Session, quiz_id: int):
        return (
            db.query(QuizQuestion)
            .filter(QuizQuestion.quiz_id == quiz_id)
            .all()
        )

    @staticmethod
    def save_attempt(
        db: Session,
        quiz_id: int,
        user_id: int,
        score: int,
        total_questions: int,
    ):
        percentage = (score / total_questions) * 100 if total_questions else 0

        attempt = QuizAttempt(
            quiz_id=quiz_id,
            user_id=user_id,
            score=score,
            total_questions=total_questions,
            percentage=percentage,
        )

        db.add(attempt)
        db.commit()
        db.refresh(attempt)

        return attempt

    @staticmethod
    def get_attempts(db: Session, user_id: int):
        return (
            db.query(QuizAttempt)
            .filter(QuizAttempt.user_id == user_id)
            .order_by(QuizAttempt.attempted_at.desc())
            .all()
        )