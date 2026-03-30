import streamlit as st

st.subheader('Data Analytics Platform - Class 10')

if "visibility" not in st.session_state:
    st.session_state.disabled = False

radio_button = st.radio("Choose your Language",
                        ["Python | R :white_circle:",
                         "Java | C :black_circle:",
                         "HTML | CSS | JavaScript :red_circle:",
                         "Dart | Flutter :large_blue_circle:",
                         "SQL :diamond_shape_with_a_dot_inside:"],
                         index=None,
                         key='visibility',
                         disabled=st.session_state.disabled)

st.session_state.disabled = True

if radio_button == "Python | R :white_circle:":
    st.write("You selected Python | R")
    st.link_button('Click', '')
elif radio_button == "Java | C :black_circle:":
    st.write("You selected Java | C")
    st.link_button('Click', '')
elif radio_button == "HTML | CSS | JavaScript :red_circle:":
    st.write("You selected HTML | CSS | JavaScript")
    st.link_button('Click', '')
elif radio_button == "Dart | Flutter :large_blue_circle:":
    st.write("You selected Dart | Flutter")
    st.link_button('Click', '')
elif radio_button == "SQL :diamond_shape_with_a_dot_inside:":
    st.write("You selected SQL")
    st.link_button('Click', '')
else:
    print('Not Selected')