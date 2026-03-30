import streamlit as st

image_list = ['programming.png', 'code.png']
caption_list = ['Programming','Code']
st.header("Welcome to Alyson's Code")
st.image('programming.png', width=100)
st.image('code.png', width=100)

st.image(image=image_list,width=100,caption=caption_list) # Image side by side to the website
st.subheader("Alyson's code is a youtube channel that\
             shares educational videos about computer science")

st.link_button("Go to Alyson's Code Youtube channel!",
               'https://www.youtube.com/')