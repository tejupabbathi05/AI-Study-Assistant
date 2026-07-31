from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models import QuizAttempt


class ProgressService:

    @staticmethod
    def get_statistics(db: Session, user_id: int):

        attempts = (
            db.query(QuizAttempt)
            .filter(QuizAttempt.user_id == user_id)
            .all()
        )

        total_quizzes = len(attempts)

        if total_quizzes == 0:
            return {
                "total_quizzes": 0,
                "average_score": 0,
                "best_score": 0,
                "recent_attempts": []
            }

        average_score = (
            db.query(func.avg(QuizAttempt.percentage))
            .filter(QuizAttempt.user_id == user_id)
            .scalar()
        )

        best_score = (
            db.query(func.max(QuizAttempt.percentage))
            .filter(QuizAttempt.user_id == user_id)
            .scalar()
        )

        return {
            "total_quizzes": total_quizzes,
            "average_score": round(average_score, 2),
            "best_score": round(best_score, 2),
            "recent_attempts": attempts[-10:]
        }