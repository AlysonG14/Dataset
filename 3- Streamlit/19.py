import streamlit as st

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Basketball", "Muay Thai", "Cycle", "Gym", "Swimming"])

with tab1:
    st.header('BasketBall')
    st.image('BasketBall.avif', width=400)
    st.write('I like to play BasketBall!')

with tab2:
    st.header('Muay Thai')
    st.image('MuayThai.jpeg', width=400)
    st.write('I like to fight with Muay Thai!')

with tab3:
    st.header('Cycle')
    st.image('Cycle.jpg', width=400)
    st.write('I like to play Cycle!')

with tab4:
    st.header('Gym')
    st.image('Gym.avif', width=400)
    st.write('I like to do Gym!')

with tab5:
    st.header('Swimming')
    st.image('Swimming.jpg', width=400)
    st.write('I like to Swim!')