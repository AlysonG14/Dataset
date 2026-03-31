import streamlit as st

options = st.multiselect(
    'What are your favorite companies?',
    ['Bosch', 'Microsoft', 'Cinesystem', 'Amazon', 'IBM', 'Google', 'Avast'],
    ['Bosch', 'Cinesystem']
)

size = st.slider('Set Image Size',100,400)

for x in options:
    if x == 'Bosch':
        st.image(r'https://reparaassistenciatecnica.com.br/wp-content/uploads/2021/11/bosch-logo-png-transparent.png', width=size)
    elif x == 'Cinesystem':
        st.image(r'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZOQdX1Rw2JsYECNfslpEmJ318j9hrDVlhig&s', width=size)
    elif x == 'Microsoft':
        st.image(r'https://blog.microsafe.com.br/wp-content/uploads/2012/08/MSFT_logo_Web1.jpg', width=size)
    elif x == 'IBM':
        st.image(r'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUJbxuh5HLL3yL8aWqeRbOKzD6u6nriF5CWQ&s', width=size)
    elif x == 'Amazon':
        st.image(r'https://cdn2.downdetector.com/static/uploads/logo/amazon.png', width=size)
    elif x == 'Google':
        st.image(r'https://static.wikia.nocookie.net/chile/images/5/51/Google.png/revision/latest/scale-to-width-down/1200?cb=20250510183518&path-prefix=es', width=size)
    elif x == 'Avast':
        st.image(r'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Avast_logo_2021.svg/1280px-Avast_logo_2021.svg.png', width=size)

st.write('Size: ',size)