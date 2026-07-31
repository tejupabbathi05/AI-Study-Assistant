import streamlit as st

from backend.database import SessionLocal
from backend.services.study_service import StudyService

from utils.auth import is_logged_in
from utils.styles import load_css

from components.sidebar import show_sidebar


st.set_page_config(
    page_title="My Study Plans",
    page_icon="📖",
    layout="wide"
)

load_css()

if not is_logged_in():
    st.switch_page("pages/Login.py")

show_sidebar()

db = SessionLocal()

# =====================================================
# PAGE HEADER
# =====================================================

st.title("My Study Plans")
st.caption("View, manage and organize all your AI-generated study plans.")

st.divider()

plans = StudyService.get_user_study_plans(
    db,
    st.session_state["user_id"]
)

if not plans:

    st.info("You haven't created any study plans yet.")

else:

    st.subheader(f"Saved Plans ({len(plans)})")

    for plan in plans:

        with st.container(border=True):

            col1, col2 = st.columns([6, 1])

            with col1:

                st.markdown(f"### 📚 {plan.subject}")
                st.write(f"**Exam Date:** {plan.exam_date}")
                st.write(f"**Goal:** {plan.goal}")
                st.write(f"**Study Hours / Day:** {plan.hours_per_day}")

            with col2:

                if st.button(
                    "Delete",
                    key=f"delete_{plan.id}",
                    use_container_width=True
                ):

                    StudyService.delete_study_plan(
                        db,
                        plan.id
                    )

                    st.success("Study Plan deleted successfully.")
                    st.rerun()

            st.divider()

            st.markdown(plan.study_plan)

db.close()