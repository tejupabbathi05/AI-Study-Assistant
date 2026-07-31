import streamlit as st


def feature_card(title, description, button_text, page):

    with st.container(border=True):

        st.subheader(title)

        st.caption(description)

        st.write("")

        if st.button(
            button_text,
            key=f"btn_{page}",
            use_container_width=True,
        ):
            st.switch_page(page)