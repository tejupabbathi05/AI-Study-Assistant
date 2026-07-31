import streamlit as st


def login_user(user):
    st.session_state.logged_in = True
    st.session_state.user_id = user.id
    st.session_state.user_name = user.full_name
    st.session_state.user_email = user.email


def logout_user():
    keys = [
        "logged_in",
        "user_id",
        "user_name",
        "user_email",
        "chat_history",
        "questions",
        "quiz_id",
    ]

    for key in keys:
        st.session_state.pop(key, None)


def is_logged_in():
    return st.session_state.get("logged_in", False)


def require_login():
    if not is_logged_in():
        st.switch_page("pages/Login.py")
        st.stop()