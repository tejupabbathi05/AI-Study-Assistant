import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stSidebar"]{
    display:none;
}

.main{
    background: linear-gradient(135deg,#eef4ff,#ffffff);
}

.title{
    text-align:center;
    font-size:52px;
    font-weight:700;
    color:#1f3c88;
    margin-top:90px;
}

.subtitle{
    text-align:center;
    font-size:26px;
    font-weight:600;
    margin-top:15px;
}

.caption{
    text-align:center;
    color:#666666;
    font-size:18px;
    margin-top:20px;
    line-height:1.8;
}

div.stButton > button{
    display:block;
    margin:auto;
    margin-top:50px;
    width:230px;
    height:60px;
    border-radius:15px;
    font-size:20px;
    font-weight:bold;
    background:#2563eb;
    color:white;
    border:none;
}

div.stButton > button:hover{
    background:#1d4ed8;
    color:white;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🎓 AI STUDY ASSISTANT</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Welcome to AI Study Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <div class="caption">
    Plan smarter, learn faster, and track your<br>
    progress—all in one intelligent workspace.
    </div>
    ''',
    unsafe_allow_html=True
)

st.write("")

if st.button("Get Started →"):
    st.switch_page("pages/Login.py")