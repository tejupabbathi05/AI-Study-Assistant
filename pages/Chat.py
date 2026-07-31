import streamlit as st

from agents.tutor_graph import tutor_graph

from utils.auth import require_login
from utils.styles import load_css

from components.sidebar import show_sidebar


st.set_page_config(
    page_title="AI Tutor",
    page_icon="🤖",
    layout="wide"
)

load_css()

require_login()

show_sidebar()

# =====================================================
# PAGE HEADER
# =====================================================

st.title("AI Tutor")
st.caption("Ask questions, clear your doubts, and learn with your AI study companion.")

st.divider()

# =====================================================
# CHAT
# =====================================================

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.container(border=True):

    if not st.session_state.chat_history:

        st.info(
            "👋 Welcome! Ask me anything about your studies to get started."
        )

    for message in st.session_state.chat_history:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

question = st.chat_input(
    "Ask anything about your studies..."
)

if question:

    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": question
        }
    )

    st.rerun()

# =====================================================
# GENERATE RESPONSE
# =====================================================

if (
    st.session_state.chat_history
    and st.session_state.chat_history[-1]["role"] == "user"
):

    question = st.session_state.chat_history[-1]["content"]

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = tutor_graph.invoke(
                {
                    "question": question
                }
            )

        st.markdown(result["answer"])

    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )

    st.rerun()