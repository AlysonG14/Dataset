import streamlit as st

col1, col2, col3, col4 = st.columns(4)

with st.sidebar:
    add_selectbox = st.selectbox(
        "How would you like to be connected?",
        ("Name", "Mobile Phone", "Home Phone", "Email")
    )
    if add_selectbox == 'Name':
        name = st.text_input("What's your name?")
        surname = st.text_input("What's your surname?")

        if st.button("Show"):
            st.write('Hello {} {}. Welcome to course language programming'.format(name, surname))
        
    elif add_selectbox == 'Mobile Phone':
        mobile_phone = st.text_input("What's your mobile phone?")

        if st.button("Show"):
            st.write('Mobile Phone: {}'.format(mobile_phone))

    elif add_selectbox == 'Home Phone':
        home_phone = st.text_input("What's your home phone?")

        if st.button("Show"):
            st.write('Home Phone: {}'.format(home_phone))

    elif add_selectbox == 'Email':
        email = st.text_input("What's your email?")

        if st.button("Show"):
            st.write('Email: {}'.format(email))

    color = st.color_picker('#00DE80')

    st.markdown(f"<span style='color:{color}'>Send</span>", unsafe_allow_html=True)


size_input = st.slider("Icon's Size",100,400)

with col1:
    st.header('HTML')
    st.image('HTML5.png', width=size_input)
    st.link_button('HTML Course', r'https://www.w3schools.com/html/')

with col2:
    st.header('CSS')
    st.image('CSS3.png', width=size_input)
    st.link_button('CSS Course', r'https://www.w3schools.com/css/default.asp')


with col3:
    st.header('JavaScript')
    st.image('JavaScript.jpg', width=size_input)
    st.link_button('JavaScript Course', r'https://www.w3schools.com/js/default.asp')


with col4:
    st.header('Python')
    st.image('Python.png', width=size_input)
    st.link_button('Python Course', r'https://www.w3schools.com/python/default.asp')


# with col5:
#     st.header('Java')
#     st.image('Java.png')
#     st.link_button('Java Course', r'https://www.w3schools.com/java/default.asp')
# 
# 
# with col6:
#     st.header('Dart')
#     st.image('Dart.png')
#     st.link_button('Dart Course', r'https://www.geeksforgeeks.org/dart/dart-tutorial/')
# 
# 
# with col7:
#     st.header('C')
#     st.image('C.png')
#     st.link_button('C Course', r'https://www.w3schools.com/c/index.php')
# 
# 
# with col8:
#     st.header('R')
#     st.image('R.svg')
#     st.link_button('R Course', r'https://www.w3schools.com/r/')
# 
# 
# with col9:
#     st.header('MYSQL')
#     st.image('MYSQL.png')
#     st.link_button('MYSQL Course', r'https://www.w3schools.com/mysql/default.asp')
