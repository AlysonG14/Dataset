import streamlit as st
import datetime

name = st.text_input('Name')

company_name = st.text_input('Company Name')

start_date = st.date_input('Starting Date',datetime.date(2019,7,6))

end_date = st.date_input('Ending Date',datetime.date(2020,7,6))

# multipy_data = (start_date + end_date) / 365 * 60

show_button = st.button('Show')

if show_button:
    st.write('Hey {}! You worked at {} for {} days.'.format(name, company_name))