import streamlit as st
from utils.auth import logout_user


def menu_button(text, page):

    if st.button(
        text,
        use_container_width=True,
        key=page
    ):
        st.switch_page(page)


def show_sidebar():

    with st.sidebar:

        st.markdown("")

        st.markdown(
            "# 🎓 AI Study Assistant"
        )

        st.caption("Your AI Learning Companion")

        st.markdown("---")

        st.markdown("### 👤 Profile")

        st.write(f"**{st.session_state.get('user_name','User')}**")

        st.caption("Student")

        st.markdown("---")

        st.markdown("### Navigation")

        menu_button(
            "🏠 Dashboard",
            "pages/Dashboard.py"
        )

        menu_button(
            "📚 Study Planner",
            "pages/Study_Planner.py"
        )

        menu_button(
            "📖 My Study Plans",
            "pages/My_Study_Plans.py"
        )

        menu_button(
            "🤖 AI Tutor",
            "pages/Chat.py"
        )

        menu_button(
            "📝 Quiz",
            "pages/Quiz.py"
        )

        menu_button(
            "📈 Progress",
            "pages/Progress.py"
        )

        menu_button(
            "⚙️ Settings",
            "pages/Settings.py"
        )

        st.markdown("---")

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):
            logout_user()
            st.switch_page("pages/Login.py")