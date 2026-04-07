import streamlit as st

st.header('Python Tutorial')

documentation01 = r'www.w3schools.com/python/'
documentation02 = r'https://www.w3schools.com/python/python_syntax.asp'
documentation03 = r'https://www.w3schools.com/python/python_variables.asp'

st.markdown("""
    
    <style>
            
    img {
        width: 100px;
        height: 200px;
        justify-content: center;
        display: flex;
        border-radius: 50%;
        transition: 1s;
        cursor: pointer;
        
        }
            
    img:hover {
        transform: scale(1.1);
        border: 1px solid green;
        
        }
            
    </style>

""", unsafe_allow_html=True
)



with st.expander("Python Course"):
    with st.container(border=True):
        st.image('Python.png', width=200)
        st.write('Python is a programming language that lets you work quickly and integrate systems more effectively.')

        with st.expander(f"Course 01"):
            st.write('Documentation - Part 01')
            st.link_button("Documentation 01", documentation01)

        with st.expander("Course 02"):
            st.write('Documentation - Part 02')
            st.link_button("Documentation 02", documentation02)

        with st.expander("Course 03 "):
            st.write("Documentation - Part 03")
            st.link_button("Documentation 03", documentation03)
        
