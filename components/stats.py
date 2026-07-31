import streamlit as st


def stat_card(label, value, delta=None):

    with st.container():

        if delta is not None:
            st.metric(
                label=label,
                value=value,
                delta=delta
            )
        else:
            st.metric(
                label=label,
                value=value
            )