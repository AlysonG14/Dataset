import streamlit as st

st.header('Choose your image: ')

image_info = [{
        'IMAGE_NAME': 'Koala',
        'IMAGE_YEAR': '2008',

    }, {
        'IMAGE_NAME': 'Desert',
        'IMAGE_YEAR': '2004',


    }, {
        'IMAGE_NAME': 'Phone',
        'IMAGE_YEAR': '1994',


    }, {
        'IMAGE_NAME': 'Penguins',
        'IMAGE_YEAR': '2000',


    }, {
        'IMAGE_NAME': 'Lighthouse',
        'IMAGE_YEAR': '2009',


    }
]

option = [
    f"{img['IMAGE_NAME']} {img['IMAGE_YEAR']}"
    for img in image_info
]

options = st.selectbox('Which image did you like', option)


for img in image_info:
    label = f"{img['IMAGE_NAME']} {img['IMAGE_YEAR']}"


    if options == label:
        st.image(
            f"C:/Users/ATL8CA/Pictures/{img['IMAGE_NAME']}.jpg",
            width=300,
            caption=f"NAME: {img['IMAGE_NAME']} YEAR: {img['IMAGE_YEAR']}"
        )

st.write(options)
