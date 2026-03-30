import streamlit as st

car_types = ['toyota', 'fiat', 'ford', 'onix', 'palio', 'bmw', 'fusca', 'mustang']

car = st.text_input('Type an car') # input

button = st.button('Check Availability')

if (button == True):
    have_it = car.lower() in car_types
    if have_it:
        st.write('We have that car!')
    else:
        st.write("We don't have that car.")

st.image('https://upload.wikimedia.org/wikipedia/commons/b/b6/Image_created_with_a_mobile_phone.png', caption='This is a offical image')
file_name = st.text_input('Enter file name')
st.write(file_name)

with open(r'c:\Users\ATL8CA\Pictures\phone.png', 'rb') as file:
    btn = st.download_button(
        label='Download Image',
        data=file,
        file_name=file_name,
        mime=r'C:\Users\ATL8CA\Downloads',
    )

