import pandas as pd
import streamlit as st

st.title("Data Analytics Platform")
st.subheader("Name: Alyson Pereira dos Santos")
data = 'print("Hello World")'

st.code(data)

def trafficLight():
    traffic_light = ['red', 'yellow', 'green']

    choose = st.text_input('Type the traffic light color')

    if st.button('Check Avaliability'):
        have_it = choose.lower() in traffic_light
        'We have this traffic light' if have_it else 'We don\'t have this traffic light'
        return True
    else:
        print("We don't have this traffic light!")
        return False
    
check = st.button('Exercise 01')
close = ''

if check:
    trafficLight()
    close = st.button('Close')












    
    