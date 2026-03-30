import streamlit as st

st.header('Choose your image: ')

image_info = [{
        'IMAGE_NAME': 'Koala',
        'IMAGE_YEAR': '2008',
        'IMAGE_LINK': ''
    }, {
        'IMAGE_NAME': 'Desert',
        'IMAGE_YEAR': '2004',
        'IMAGE_LINK': ''

    }, {
        'IMAGE_NAME': 'Phone',
        'IMAGE_YEAR': '1994',
        'IMAGE_LINK': ''

    }, {
        'IMAGE_NAME': 'Penguins',
        'IMAGE_YEAR': '2000',
        'IMAGE_LINK': ''

    }, {
        'IMAGE_NAME': 'Lighthouse',
        'IMAGE_YEAR': '2009',
        'IMAGE_LINK': ''

    }
]

option = st.selectbox('Which image did you like?', 
                      [image_info[0]['IMAGE_NAME'] + " " + image_info[0]['IMAGE_YEAR']],
                      image_info[1]['IMAGE_NAME'] + " " + image_info[1]['IMAGE_YEAR'],
                      image_info[2]['IMAGE_NAME'] + " " + image_info[2]['IMAGE_YEAR'],
                      image_info[3]['IMAGE_NAME'] + " " + image_info[3]['IMAGE_YEAR'],
                      image_info[4]['IMAGE_NAME'] + " " + image_info[4]['IMAGE_YEAR']
                      
                      )

if option == image_info[0]['IMAGE_NAME'] + " " + image_info[0]['IMAGE_YEAR']:
    st.image(r"C:\Users\ATL8CA\Pictures\Koala.jpg", width=300, caption='NAME: ' + str(image_info[0]['IMAGE_NAME']) + " " + \
                                                                       'YEAR: ' + int(image_info[0]['IMAGE_YEAR']))

elif option == image_info[1]['IMAGE_NAME'] + " " + image_info[1]['IMAGE_YEAR']:
    st.image(r"C:\Users\ATL8CA\Pictures\Desert.jpg", width=300, caption='NAME: ' + str(image_info[1]['IMAGE_NAME']) + " " + \
                                                                        'YEAR: ' + int(image_info[1]['IMAGE_YEAR']))

elif option == image_info[2]['IMAGE_NAME'] + " " + image_info[2]["IMAGE_YEAR"]:
    st.image(r"C:\Users\ATL8CA\Pictures\phone.png", width=300, caption='NAME: ' + str(image_info[2]['IMAGE_NAME']) + " " + \
                                                                       'YEAR: ' + int(image_info[2]['IMAGE_YEAR']))

elif option == image_info[3]['IMAGE_NAME'] + " " + image_info[3]["IMAGE_YEAR"]:
    st.image(r"C:\Users\ATL8CA\Pictures\Penguins.jpg", width=300, caption='NAME: ' + str(image_info[3]['IMAGE_NAME']) + " " + \
                                                                          'YEAR: ' + int(image_info[3]['IMAGE_YEAR']))

elif option == image_info[4]['IMAGE_NAME'] + " " + image_info[4]["IMAGE_YEAR"]:
    st.image(r"C:\Users\ATL8CA\Pictures\Lighthouse.jpg", width=300, caption='NAME: ' + str(image_info[4]['IMAGE_NAME']) + " " + \
                                                                            'YEAR: ' + int(image_info[4]['IMAGE_YEAR']))
    

