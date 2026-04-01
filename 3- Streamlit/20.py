import streamlit as st

tab1, tab2, tab3 = st.tabs(['C', 'R', 'Python'])

with tab1:
    st.header('C')
    st.image('')
    st.write('I love programming C language')

with tab2:
    st.header('R')
    st.image('')
    st.write('I love programming R language')

with tab3:
    st.header('Python')
    st.image('')
    st.write('I love programming Python language')