from sqlalchemy import func

from backend.models import (
    StudySession,
    QuizAttempt,
    Progress
)


class DashboardService:

    @staticmethod
    def get_dashboard_stats(db, user_id):

        study_plans = (
            db.query(StudySession)
            .filter(
                StudySession.user_id == user_id
            )
            .count()
        )

        quiz_attempts = (
            db.query(QuizAttempt)
            .filter(
                QuizAttempt.user_id == user_id
            )
            .count()
        )

        average_score = (
            db.query(
                func.avg(QuizAttempt.percentage)
            )
            .filter(
                QuizAttempt.user_id == user_id
            )
            .scalar()
        )

        latest_progress = (
            db.query(Progress)
            .filter(
                Progress.user_id == user_id
            )
            .order_by(
                Progress.created_at.desc()
            )
            .first()
        )

        return {

            "study_plans": study_plans,

            "quiz_attempts": quiz_attempts,

            "average_score": (
                round(average_score, 1)
                if average_score
                else 0
            ),

            "overall_score": (
                latest_progress.overall_score
                if latest_progress
                and latest_progress.overall_score
                else 0
            )
        }