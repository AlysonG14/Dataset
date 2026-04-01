import streamlit as st
import datetime

name = st.text_input('Name')

company_name = st.text_input('Company Name')

start_date = st.date_input('Starting Date',datetime.date(2019,7,6))

end_date = st.date_input('Ending Date',datetime.date(2020,7,6))

pt1 = str(start_date).split('-')
pt2 = str(end_date).split('-')

t1 = datetime.date(year=int(pt1[0]), month=int(pt1[1]), day=int(pt1[2]))
t2 = datetime.date(year=int(pt2[0]), month=int(pt2[1]), day=int(pt2[2]))

show_button = st.button('Show')

if show_button:
    st.write('Hey {}! You worked at {} for {} days.'.format(name, company_name, (t2-t1).days))