import streamlit as st

from utils.auth import require_login, logout_user
from utils.styles import load_css

from components.sidebar import show_sidebar

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

load_css()

require_login()

show_sidebar()

st.markdown("""
<div class="welcome-box">
    <div class="welcome-title">
        ⚙️ Settings
    </div>

    <div class="welcome-subtitle">
        Manage your account and application preferences.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("## 👤 Account")

st.write(f"**Name:** {st.session_state.get('user_name','')}")
st.write(f"**Email:** {st.session_state.get('user_email','')}")

st.markdown("---")

st.markdown("## ℹ️ Application")

st.info("""
AI Study Assistant helps you:

• Generate AI Study Plans

• Learn with an AI Tutor

• Take AI-generated Quizzes

• Track your Progress
""")

st.markdown("---")

st.markdown("## 🚪 Logout")

if st.button(
    "Logout",
    use_container_width=True
):
    logout_user()
    st.switch_page("pages/Login.py")