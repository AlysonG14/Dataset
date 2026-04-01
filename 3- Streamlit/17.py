import streamlit as st

st.header('**Welcome to Streamlit Course!**')
st.video(r'https://www.youtube.com/watch?v=pWjmpSD-ph0')


with st.sidebar:
    add_selectbox = st.selectbox(
        "How would you like to be contacted?",
        ("Mobile Phone", 'Home Phone', 'Email')
    )

    add_input = st.text_input("Info")

    add_radio = st.radio(
        "Choose the shippig method",
        ("Standard (5-15) days", "Express (2-5 days) ")
    )

    send_button = st.button('Send')

if send_button:
    st.sidebar.write('Send button clicked!')

