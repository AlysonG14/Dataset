import streamlit as st

image_list = ['code.png', 'programming.png', 'data.png', 'publish.png']
caption_list = ['Code', 'Programmer', 'Data', 'Publisher']
st.header('Welcome to Data Analytics Platform')
# st.image(image=image_list, caption=capiton_list, width=100)

checks = st.columns(2) # columns --> set what types columns do you want

with checks[0]:
    images = st.checkbox('Do you want to see photos?')

with checks[1]:
    codes = st.checkbox('Do you want to see codes?')


def checkbox():

    checks_2 = st.columns(2)

    with checks_2[0]:
        if images:
            st.image(image=image_list, width=100, caption=caption_list)


    with checks_2[1]:
        if codes:
            code = 'print("My name is Alyson Pereira dos Santos")'
            st.code(code)

checkbox()
