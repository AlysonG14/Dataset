import streamlit as st

color = st.color_picker('Pick a Color', '#000000')

st.markdown(f"<span style='color:{color}'> Welcom to my Company Alyson! </span>", 
            unsafe_allow_html=True)

st.write('The current color is: ',color)

