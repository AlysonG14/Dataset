import streamlit as st


with st.expander("Programming Language"):

    with st.expander('Python'):
        with st.container(border=True):
            st.image('Python.png', width=150)
            st.write('This is a Python container!')

    with st.expander('Java'):
        with st.container(border=True):
            st.image('Java.png', width=150)
            st.write('This is a Java container!')

    with st.expander('JavaScript'):
        with st.container(border=True):
            st.image('JavaScript.jpg', width=150)
            st.write('This is a JavaScript container!')

