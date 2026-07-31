import streamlit as st


def load_css():

    st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

/* =====================================================
GLOBAL
===================================================== */

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
    background:#0F0F17;
    color:white;
}

#MainMenu,
header,
footer{
    visibility:hidden;
}

[data-testid="stSidebarNav"]{
    display:none;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1400px;
}

/* =====================================================
TEXT
===================================================== */

h1,h2,h3,h4,h5,h6{
    color:white !important;
    font-weight:700;
}

p,
span,
label,
small,
div{
    color:#E5E7EB;
}

/* =====================================================
SIDEBAR
===================================================== */

section[data-testid="stSidebar"]{

    background:#171726;
    border-right:1px solid #2D2D44;
}

section[data-testid="stSidebar"] *{

    color:white !important;
}

section[data-testid="stSidebar"] .stButton{

    margin-bottom:8px;
}

section[data-testid="stSidebar"] .stButton>button{

    background:transparent !important;

    color:white !important;

    border:1px solid transparent !important;

    border-radius:12px;

    height:46px;

    text-align:left;

    font-weight:600;
}

section[data-testid="stSidebar"] .stButton>button:hover{

    background:#7C3AED !important;

    border-color:#8B5CF6 !important;
}

/* =====================================================
BUTTONS
===================================================== */

.stButton>button{

    width:100%;

    height:46px;

    border:none !important;

    border-radius:12px;

    background:#8B5CF6 !important;

    color:white !important;

    font-weight:600;

    font-size:15px;
}

.stButton>button:hover{

    background:#7C3AED !important;
}

.stButton>button span,
.stButton>button p{

    color:white !important;
}

/* =====================================================
INPUTS
===================================================== */

.stTextInput input,
.stTextArea textarea{

    background:#1A1A28 !important;

    color:white !important;

    border:1px solid #3F3F5A !important;

    border-radius:12px;
}

/* =====================================================
SELECT BOX
===================================================== */

.stSelectbox div[data-baseweb="select"]{

    background:#1A1A28 !important;

    color:white !important;
}

/* =====================================================
METRIC CARDS
===================================================== */

[data-testid="stMetric"]{

    background:#6D28D9;

    border:none;

    border-radius:18px;

    padding:18px;

    box-shadow:0 8px 25px rgba(109,40,217,.35);
}

[data-testid="stMetricLabel"]{

    color:white !important;

    font-weight:600;
}

[data-testid="stMetricValue"]{

    color:white !important;

    font-size:34px !important;

    font-weight:700 !important;
}

/* =====================================================
CONTAINERS
===================================================== */

div[data-testid="stVerticalBlockBorderWrapper"]{

    margin-bottom:18px;
}

/* =====================================================
WELCOME CARD
===================================================== */

.welcome-box{

    background:#6D28D9;

    border-radius:20px;

    padding:30px;

    margin-bottom:25px;

    box-shadow:0 10px 30px rgba(109,40,217,.4);
}

.welcome-title{

    color:white !important;

    font-size:34px;

    font-weight:700;
}

.welcome-subtitle{

    color:#E9D5FF !important;

    font-size:17px;
}

/* =====================================================
EXPANDERS
===================================================== */

.streamlit-expanderHeader{

    color:white !important;
}

/* =====================================================
DATAFRAME
===================================================== */

[data-testid="stDataFrame"]{

    background:#171726;
}

/* =====================================================
SCROLLBAR
===================================================== */

::-webkit-scrollbar{

    width:8px;
}

::-webkit-scrollbar-thumb{

    background:#8B5CF6;

    border-radius:20px;
}

/* =====================================================
SUCCESS / ERROR
===================================================== */

.stAlert{

    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)