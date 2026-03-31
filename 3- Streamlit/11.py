import streamlit as st
import pandas as pd

list = []

IMAGES_HULK = [
    {   
        'IMAGE': r'https://i1.wp.com/silverscreencapture.com/wp-content/uploads/2003/04/6BC5DD95-5511-478C-9F22-020FA7539621.jpeg?zoom=3&resize=672%2C372',
        'YEAR': 2003,
        'RAGE': '30/100' ,
        'ENDURANCE': '500/500',
        'STRENGTH': '800/1000',
    },
    {
        'IMAGE': r'https://www.intofilm.org/intofilm-production/scaledcropped/1096x548https:/s3-eu-west-1.amazonaws.com/images.cdn.filmclub.org/film__3508-the-incredible-hulk--hi_res-a7620a5e.jpg/film__3508-the-incredible-hulk--hi_res-a7620a5e.jpg',
        'YEAR': 2008,
        'RAGE': '80/100' ,
        'ENDURANCE': '200/500',
        'STRENGTH': '500/1000',
    },
    {
        'IMAGE': r'https://wallpaperaccess.com/full/2190585.jpg',
        'YEAR': 2012,
        'RAGE': '70/100' ,
        'ENDURANCE': '300/500',
        'STRENGTH': '560/1000',

    }
]

name = st.text_input("What's your name: ")

surname = st.text_input("What's your surname: ")

hulk = st.text_input('Choose the best hulk scene have you watched: ')

if hulk == 2008:
    st.write('ROOOOAAAAARRRRRRRRR')
    st.image()
elif hulk == 2003:
    st.write('')
    st.image('')
elif hulk == 2012:
    st.write('')
    st.image('')

txt = st.text_area(
    "Text to analyze",
    "",placeholder='Write about your life!',max_chars=361
)
analyze_button = st.button('Analyze')

if analyze_button:
    st.write('Congratulations: {} {}. You wrote: {}'.format(name,surname,txt))
    text_split = txt.split(sep='')
    for word in text_split:
        list.append(word)
    st.write(f'You wrote: {len(txt)} characters. You wrote {len(list)} words.')