import streamlit as st

name = st.text_input("What's your name?")

surname = st.text_input("What's your surname?")

button = st.button('Show')

if button == True:
    st.write(f'Welcome {name} {surname}, this web page :computer:')
