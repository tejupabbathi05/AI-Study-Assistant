from backend.models import StudySession


class StudyService:

    @staticmethod
    def save_study_plan(
        db,
        user_id,
        subject,
        exam_date,
        hours_per_day,
        goal,
        study_plan,
    ):

        session = StudySession(
            user_id=user_id,
            subject=subject,
            exam_date=str(exam_date),
            hours_per_day=hours_per_day,
            goal=goal,
            study_plan=study_plan,
        )

        db.add(session)
        db.commit()
        db.refresh(session)

        return session

    @staticmethod
    def get_user_study_plans(db, user_id):

        return (
            db.query(StudySession)
            .filter(StudySession.user_id == user_id)
            .order_by(StudySession.created_at.desc())
            .all()
        )

    @staticmethod
    def delete_study_plan(db, plan_id):

        plan = (
            db.query(StudySession)
            .filter(StudySession.id == plan_id)
            .first()
        )

        if plan:
            db.delete(plan)
            db.commit()