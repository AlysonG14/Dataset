import streamlit as st
import time

time_input = st.text_input('Enter a time')
button = st.button('Start')

if button:

    with st.empty():
        for seconds in range(int(time_input)):
            seconds += 1
            st.write('{} seconds has been passed.'.format(seconds))
            time.sleep(1)
            # if seconds == time_input:
        st.image('https://static.vecteezy.com/system/resources/thumbnails/045/995/954/small/a-golden-trophy-with-a-star-on-top-png.png', width=300)
        # st.write("You're champion! Take this prize!")