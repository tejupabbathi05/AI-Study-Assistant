from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship

from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    study_sessions = relationship(
        "StudySession",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    progress = relationship(
        "Progress",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    quiz_attempts = relationship(
        "QuizAttempt",
        back_populates="user",
        cascade="all, delete-orphan"
    )


class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    subject = Column(String(150), nullable=False)
    exam_date = Column(String(50), nullable=False)
    hours_per_day = Column(Integer, nullable=False)
    goal = Column(Text, nullable=False)
    study_plan = Column(Text, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship(
        "User",
        back_populates="study_sessions"
    )

    quizzes = relationship(
        "Quiz",
        back_populates="study_session",
        cascade="all, delete-orphan"
    )


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)

    study_session_id = Column(
        Integer,
        ForeignKey("study_sessions.id"),
        nullable=False
    )

    difficulty = Column(String(20), nullable=False)

    total_questions = Column(Integer, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    study_session = relationship(
        "StudySession",
        back_populates="quizzes"
    )

    questions = relationship(
        "QuizQuestion",
        back_populates="quiz",
        cascade="all, delete-orphan"
    )

    attempts = relationship(
        "QuizAttempt",
        back_populates="quiz",
        cascade="all, delete-orphan"
    )


class QuizQuestion(Base):
    __tablename__ = "quiz_questions"

    id = Column(Integer, primary_key=True, index=True)

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id"),
        nullable=False
    )

    question = Column(Text, nullable=False)

    option_a = Column(Text, nullable=False)
    option_b = Column(Text, nullable=False)
    option_c = Column(Text, nullable=False)
    option_d = Column(Text, nullable=False)

    correct_answer = Column(String(1), nullable=False)

    explanation = Column(Text)

    quiz = relationship(
        "Quiz",
        back_populates="questions"
    )


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"

    id = Column(Integer, primary_key=True, index=True)

    quiz_id = Column(
        Integer,
        ForeignKey("quizzes.id"),
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    score = Column(Integer, nullable=False)

    total_questions = Column(Integer, nullable=False)

    percentage = Column(Float, nullable=False)

    attempted_at = Column(DateTime, default=datetime.utcnow)

    quiz = relationship(
        "Quiz",
        back_populates="attempts"
    )

    user = relationship(
        "User",
        back_populates="quiz_attempts"
    )


class Progress(Base):
    __tablename__ = "progress"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    weak_topics = Column(Text)

    strong_topics = Column(Text)

    overall_score = Column(Integer)

    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship(
        "User",
        back_populates="progress"
    )