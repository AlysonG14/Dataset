import streamlit as st

first_team = st.text_input('First Team')
second_team = st.text_input('Second Team')

time = st.time_input('Set an alarm for',value=None)

if st.button('Show'):
    st.write(f'The match between the {first_team} and the {second_team} will start at {time}')