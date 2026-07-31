import streamlit as st

from backend.database import SessionLocal
from backend.services.auth_service import AuthService
from utils.auth import login_user

st.set_page_config(
    page_title="Login - AI Study Assistant",
    page_icon="🎓",
    layout="centered"
)

db = SessionLocal()

st.markdown("""
<style>

[data-testid="stHeader"]{
    background:transparent;
}

.main{
    background:linear-gradient(135deg,#eef4ff,#ffffff);
}

.block-container{
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:38px;
    font-weight:700;
    color:#1f3c88;
}

.subtitle{
    text-align:center;
    color:#666;
    margin-bottom:30px;
    font-size:17px;
}

div[data-testid="stVerticalBlock"]{
    border-radius:18px;
}

div.stButton > button{
    width:100%;
    height:50px;
    border-radius:12px;
    font-size:17px;
    font-weight:600;
    background:#2563eb;
    color:white;
    border:none;
}

div.stButton > button:hover{
    background:#1d4ed8;
    color:white;
}

input{
    border-radius:10px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎓 AI Study Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Sign in to continue your learning journey</div>',
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])

with tab1:

    st.markdown("### Welcome Back")

    login_email = st.text_input(
        "Email",
        key="login_email"
    )

    login_password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button(
        "Login",
        use_container_width=True
    ):

        user = AuthService.login_user(
            db,
            login_email,
            login_password
        )

        if user:

            login_user(user)

            st.success("Login Successful!")

            st.switch_page("pages/Dashboard.py")

        else:

            st.error("Invalid email or password.")

with tab2:

    st.markdown("### Create Your Account")

    full_name = st.text_input(
        "Full Name"
    )

    email = st.text_input(
        "Email"
    )

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "Create Account",
        use_container_width=True
    ):

        success, message = AuthService.register_user(
            db,
            full_name,
            email,
            password
        )

        if success:

            st.success(message)

        else:

            st.error(message)