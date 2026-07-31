import streamlit as st

from agents.graph import study_graph
from backend.database import SessionLocal
from backend.services.study_service import StudyService

from utils.auth import is_logged_in
from utils.styles import load_css
from components.sidebar import show_sidebar


st.set_page_config(
    page_title="Study Planner",
    page_icon="📚",
    layout="wide"
)

load_css()

if not is_logged_in():
    st.switch_page("pages/Login.py")

show_sidebar()

db = SessionLocal()

# ======================================================
# PAGE TITLE
# ======================================================

st.title("AI Study Planner")
st.caption("Create a personalized study schedule using AI.")

st.divider()

# ======================================================
# STUDY DETAILS
# ======================================================

st.subheader("Study Details")

with st.container(border=True):

    with st.form("study_plan_form"):

        subject = st.text_input(
            "Subject",
            placeholder="Example: Operating System"
        )

        goal = st.text_area(
            "Study Goal",
            placeholder="Example: Score above 90% in the final examination.",
            height=120
        )

        col1, col2 = st.columns(2)

        with col1:

            exam_date = st.date_input(
                "Exam Date"
            )

        with col2:

            hours_per_day = st.number_input(
                "Study Hours Per Day",
                min_value=1,
                max_value=16,
                value=2
            )

        st.write("")

        submit = st.form_submit_button(
            "Generate Study Plan",
            use_container_width=True
        )

# ======================================================
# GENERATE PLAN
# ======================================================

if submit:

    if not subject.strip():

        st.error("Please enter a subject.")
        st.stop()

    if not goal.strip():

        st.error("Please enter your study goal.")
        st.stop()

    with st.spinner("Generating your personalized study plan..."):

        result = study_graph.invoke(
            {
                "subject": subject,
                "exam_date": exam_date,
                "hours_per_day": hours_per_day,
                "goal": goal,
                "study_plan": "",
            }
        )

    StudyService.save_study_plan(
        db=db,
        user_id=st.session_state["user_id"],
        subject=subject,
        exam_date=exam_date,
        hours_per_day=hours_per_day,
        goal=goal,
        study_plan=result["study_plan"],
    )

    st.success("Study Plan Generated Successfully!")
    st.divider()

    st.subheader("Generated Study Plan")

    with st.container(border=True):

        st.markdown("### Overview")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Subject:** {subject}")
            st.write(f"**Exam Date:** {exam_date}")

        with col2:
            st.write(f"**Study Hours / Day:** {hours_per_day}")
            st.write(f"**Goal:** {goal}")

        st.divider()

        st.markdown(result["study_plan"])

db.close()
    