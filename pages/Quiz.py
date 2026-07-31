import streamlit as st

from agents.quiz_graph import quiz_graph

from backend.database import SessionLocal
from backend.services.quiz_service import QuizService

from utils.auth import require_login
from utils.styles import load_css

from components.sidebar import show_sidebar


st.set_page_config(
    page_title="Quiz",
    page_icon="📝",
    layout="wide"
)

load_css()

require_login()

show_sidebar()

# =====================================================
# PAGE HEADER
# =====================================================

st.title("AI Quiz Generator")
st.caption("Generate personalized quizzes from your study plans and test your knowledge.")

st.divider()

db = SessionLocal()

plans = QuizService.get_study_plans(
    db,
    st.session_state["user_id"]
)

if not plans:

    st.warning("No study plans found. Please create a study plan first.")
    db.close()
    st.stop()

plan_map = {
    f"{p.subject} ({p.exam_date})": p
    for p in plans
}

# =====================================================
# QUIZ CONFIGURATION
# =====================================================

st.subheader("Quiz Configuration")

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:

        selected = st.selectbox(
            "Study Plan",
            list(plan_map.keys())
        )

        difficulty = st.selectbox(
            "Difficulty",
            [
                "Easy",
                "Medium",
                "Hard"
            ]
        )

    with col2:

        total_questions = st.selectbox(
            "Number of Questions",
            [
                5,
                10,
                15,
                20
            ]
        )

    st.write("")

    generate = st.button(
        "Generate Quiz",
        use_container_width=True
    )

# =====================================================
# GENERATE QUIZ
# =====================================================

if generate:

    with st.spinner("Generating your AI quiz..."):

        plan = plan_map[selected]

        result = quiz_graph.invoke(
            {
                "subject": plan.subject,
                "study_plan": plan.study_plan,
                "difficulty": difficulty,
                "total_questions": total_questions,
            }
        )

        quiz = QuizService.create_quiz(
            db=db,
            study_session_id=plan.id,
            difficulty=difficulty,
            questions_data=result["questions"],
        )

        st.session_state["quiz_id"] = quiz.id
        st.session_state["questions"] = result["questions"]

        st.success("Quiz generated successfully!")

# =====================================================
# TAKE QUIZ
# =====================================================

if "questions" in st.session_state:

    st.divider()

    st.subheader("Take Quiz")

    with st.container(border=True):

        answers = {}

        for i, q in enumerate(st.session_state["questions"]):

            st.markdown(f"**Question {i + 1}**")
            st.write(q["question"])

            options = {
                "A": q["option_a"],
                "B": q["option_b"],
                "C": q["option_c"],
                "D": q["option_d"],
            }

            answers[i] = st.radio(
                "Choose one option",
                options=list(options.keys()),
                format_func=lambda x: f"{x}. {options[x]}",
                index=None,
                key=f"q{i}"
            )

            if i != len(st.session_state["questions"]) - 1:
                st.divider()

        st.write("")

        submit = st.button(
            "Submit Quiz",
            use_container_width=True
        )

    if submit:

        if None in answers.values():

            st.warning("Please answer every question.")
            st.stop()

        score = 0

        st.divider()
        st.subheader("Results")

        with st.container(border=True):

            for i, q in enumerate(st.session_state["questions"]):

                options = {
                    "A": q["option_a"],
                    "B": q["option_b"],
                    "C": q["option_c"],
                    "D": q["option_d"],
                }

                if answers[i] == q["correct_answer"]:

                    score += 1
                    st.success(f"Question {i + 1}: Correct")

                else:

                    st.error(f"Question {i + 1}: Incorrect")
                    st.write(
                        f"**Correct Answer:** {q['correct_answer']}. {options[q['correct_answer']]}"
                    )
                    st.info(f"**Explanation:** {q['explanation']}")

            QuizService.save_attempt(
                db=db,
                quiz_id=st.session_state["quiz_id"],
                user_id=st.session_state["user_id"],
                score=score,
                total_questions=len(st.session_state["questions"]),
            )

            st.divider()

            st.success(
                f"Final Score: {score}/{len(st.session_state['questions'])}"
            )

            st.progress(
                score / len(st.session_state["questions"])
            )

            st.balloons()

db.close()