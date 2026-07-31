import streamlit as st
import pandas as pd
import plotly.express as px

from backend.database import SessionLocal
from backend.services.progress_service import ProgressService

from utils.auth import require_login
from utils.styles import load_css

from components.sidebar import show_sidebar


st.set_page_config(
    page_title="Progress Tracker",
    page_icon="📈",
    layout="wide"
)

load_css()

require_login()

show_sidebar()

# =====================================================
# PAGE HEADER
# =====================================================

st.title("Progress Tracker")
st.caption("Monitor your learning progress and quiz performance over time.")

st.divider()

db = SessionLocal()

stats = ProgressService.get_statistics(
    db,
    st.session_state["user_id"]
)

# =====================================================
# STATISTICS
# =====================================================

st.subheader("Statistics")

with st.container(border=True):

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Quizzes",
        stats["total_quizzes"]
    )

    col2.metric(
        "Average Score",
        f"{stats['average_score']}%"
    )

    col3.metric(
        "Best Score",
        f"{stats['best_score']}%"
    )

# =====================================================
# PERFORMANCE CHART
# =====================================================

st.divider()

st.subheader("Quiz Performance")

with st.container(border=True):

    if stats["recent_attempts"]:

        chart_data = []

        for i, attempt in enumerate(
            reversed(stats["recent_attempts"]),
            start=1
        ):

            chart_data.append(
                {
                    "Attempt": i,
                    "Percentage": attempt.percentage
                }
            )

        df = pd.DataFrame(chart_data)

        fig = px.line(
            df,
            x="Attempt",
            y="Percentage",
            markers=True
        )

        fig.update_layout(
            height=400,
            xaxis_title="Quiz Attempt",
            yaxis_title="Score (%)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info("No quiz attempts available.")

# =====================================================
# RECENT ATTEMPTS
# =====================================================

st.divider()

st.subheader("Recent Quiz Attempts")

if not stats["recent_attempts"]:

    st.info("No quiz attempts found.")

else:

    for i, attempt in enumerate(
        reversed(stats["recent_attempts"]),
        start=1
    ):

        with st.container(border=True):

            col1, col2 = st.columns([4, 1])

            with col1:

                st.markdown(f"### Attempt {i}")
                st.write(f"**Quiz ID:** {attempt.quiz_id}")
                st.write(f"**Score:** {attempt.score}/{attempt.total_questions}")
                st.write(f"**Percentage:** {attempt.percentage:.2f}%")

            with col2:

                st.write("**Date**")
                st.write(attempt.attempted_at)

                if attempt.percentage >= 80:
                    st.success("Excellent")

                elif attempt.percentage >= 60:
                    st.info("Good")

                else:
                    st.warning("Keep Practicing")

db.close()