import streamlit as st

st.subheader('Data Analytics Platform - Class 09')

images_list = ['code.png', 'data.png', 'programming.png', 'publish.png']
images_caption = ['Code', 'Data', 'Programming', 'Publish']

checks_code = st.columns(3)
checks_line = st.columns(3)
checks_images = st.columns(3)

def function_with_code():

    with checks_line[0]:
        code1 = st.checkbox("Do you want to see the first code?")
    with checks_line[1]:
        code2 = st.checkbox("Do you want to see the second code?")
    with checks_line[2]:
        code3 = st.checkbox("Do you want to see the third code?")

    with checks_code[0]:
        if code1:
            code1 = 'for number in range(11):\n' \
            '   print(number)\n' \
            '1\n' \
            '2\n' \
            '3\n' \
            '4\n' \
            '5\n' \
            '6\n' \
            '7\n' \
            '8\n' \
            '9\n' \
            '10'
            st.code(code1)

    with checks_code[1]:
        if code2:
            code2 = 'print("Welcome to Data Analytics Platform")'
            st.code(code2)

    with checks_code[2]:
        if code3:
            code3 =  'print(2 + 2)\n' \
            '4'
            st.code(code3)

function_with_code()

def function_with_images():
    images = st.checkbox('Do you want see the images?')

    if images:
        st.image(image=images_list, caption=images_caption, width=100)

function_with_images()

def function_with_toggle():

    checks_toggle = st.columns(3)
    
    with checks_toggle[0]:
        toggle_image = st.toggle('Enable Image')
    with checks_toggle[1]:
        toggle_audio = st.toggle('Enable Audio')
    with checks_toggle[2]:
        toggle_video = st.toggle('Enable Video')


    if toggle_video:
        st.video(r'https://www.youtube.com/watch?v=7yMwT4likZU&list=PL9HYL-VRX0oRsUB5AgNMQuKuHPpNDLBVt&index=2')

    if toggle_audio:
        st.audio()

    if toggle_image:
        st.image(r'c:\Users\ATL8CA\Pictures\phone.png')

function_with_toggle()
