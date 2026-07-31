import streamlit as st

from backend.database import SessionLocal
from backend.services.dashboard_service import DashboardService

from utils.auth import is_logged_in
from utils.styles import load_css

from components.sidebar import show_sidebar
from components.cards import feature_card

st.set_page_config(
    page_title="Dashboard",
    page_icon="🎓",
    layout="wide"
)

load_css()

if not is_logged_in():
    st.switch_page("pages/Login.py")

show_sidebar()

db = SessionLocal()

stats = DashboardService.get_dashboard_stats(
    db,
    st.session_state["user_id"]
)

# ==========================================================
# Welcome Banner
# ==========================================================

st.markdown(f"""
<div style="
background:linear-gradient(135deg,#2563EB,#3B82F6);
padding:30px;
border-radius:18px;
margin-bottom:20px;
">

<h1 style="color:white;margin:0;">
Welcome Back, {st.session_state["user_name"]} 👋
</h1>

<p style="color:white;margin-top:10px;font-size:18px;">
Continue your learning journey with your AI-powered study assistant.
</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# Overview
# ==========================================================

with st.container(border=True):

    st.subheader("Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Study Plans", stats["study_plans"])

    with c2:
        st.metric("Quiz Attempts", stats["quiz_attempts"])

    with c3:
        st.metric("Average Score", f"{stats['average_score']}%")

    with c4:
        st.metric("Overall Score", stats["overall_score"])

st.write("")

# ==========================================================
# Bottom Section
# ==========================================================

left, right = st.columns([2.3, 1])

# ------------------------
# Quick Access
# ------------------------

with left:

    with st.container(border=True):

        st.subheader("Quick Access")

        c1, c2 = st.columns(2)

        with c1:

            feature_card(
                "Study Planner",
                "Generate personalized AI study plans.",
                "Open Study Planner",
                "pages/Study_Planner.py"
            )

            feature_card(
                "Quiz",
                "Practice with AI generated quizzes.",
                "Open Quiz",
                "pages/Quiz.py"
            )

        with c2:

            feature_card(
                "My Study Plans",
                "View all your saved study plans.",
                "View Plans",
                "pages/My_Study_Plans.py"
            )

            feature_card(
                "Progress",
                "Track your learning performance.",
                "View Progress",
                "pages/Progress.py"
            )

# ------------------------
# AI Tutor
# ------------------------

with right:

    with st.container(border=True):

        st.subheader("AI Tutor")

        st.write(
            """
Ask questions, understand concepts,
and get personalized explanations
instantly with AI.
"""
        )

        st.write("")

        if st.button(
            "Start Chat",
            use_container_width=True,
            key="chat_button"
        ):
            st.switch_page("pages/Chat.py")

db.close()