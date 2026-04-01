import streamlit as st

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

with col1:
    st.header('HTML')
    st.image('HTML5.png')
    st.link_button('HTML Course', r'https://www.w3schools.com/html/')

with col2:
    st.header('CSS')
    st.image('CSS3.png')
    st.link_button('CSS Course', r'https://www.w3schools.com/css/default.asp')


with col3:
    st.header('JavaScript')
    st.image('JavaScript.jpg')
    st.link_button('JavaScript Course', r'https://www.w3schools.com/js/default.asp')


with col4:
    st.header('Python')
    st.image('Python.png')
    st.link_button('Python Course', r'https://www.w3schools.com/python/default.asp')


with col5:
    st.header('Java')
    st.image('Java.png')
    st.link_button('Java Course', r'https://www.w3schools.com/java/default.asp')


with col6:
    st.header('Dart')
    st.image('Dart.png')
    st.link_button('Dart Course', r'https://www.geeksforgeeks.org/dart/dart-tutorial/')


with col7:
    st.header('C')
    st.image('C.png')
    st.link_button('C Course', r'https://www.w3schools.com/c/index.php')


with col8:
    st.header('R')
    st.image('R.svg')
    st.link_button('R Course', r'https://www.w3schools.com/r/')


with col9:
    st.header('MYSQL')
    st.image('MYSQL.png')
    st.link_button('MYSQL Course', r'https://www.w3schools.com/mysql/default.asp')
