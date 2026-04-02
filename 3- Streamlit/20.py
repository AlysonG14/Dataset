import streamlit as st

tab1, tab2, tab3 = st.tabs(['JavaScript', 'Java', 'Python'])

with tab1:
    st.header('JavaScript')
    st.image('JavaScript.jpg', width=200)
    with st.expander("See explanation"):
        st.write('JavaScript is a scripting or programming language that allows you to implement complex features on web pages — every time a web page does more than just sit there and display static information for you to look at — displaying timely content updates, interactive maps, animated 2D/3D graphics, scrolling video jukeboxes, etc.')

with tab2:
    st.header('Java')
    st.image('Java.png', width=200)
    with st.expander("See explanation"):
        st.write('Java is the No. 1 development language and platform It reduces costs, abbreviates development schedules, motivates innovation, and improves application services.')

with tab3:
    st.header('Python')
    st.image('Python.png', width=200)
    with st.expander("See explanation"):
        st.write('Python is a programming language that lets you work quickly and integrate systems more effectively.')
    

