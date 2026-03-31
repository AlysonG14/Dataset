# import pandas as pd
# import streamlit as st
# import matplotlib.pyplot as plt

# fruits = {
#     'Fruit': ['Banana', 'Orange', 'Cocknut', 'Apple', 'Apple', 'Apple'],
#     'Quantity': [2, 5, 8, 10, 10, 10]
# }
# 
# df = pd.DataFrame(fruits)
# 
# print(df['Fruit'].unique())
# print(df['Quantity'].unique())
# 
# # create a dropdown
# filter_fruits = st.selectbox('Select the fruit', fruits)
# 
# 
# # filter the only values fruits
# filtered_df = df[df['Fruit'] == filter_fruits]
# 
# # build a chart
# fig, ax = plt.subplots()
# ax.plot(filtered_df['Fruit'],
#         filtered_df['Quantity'])
# 
# # set the labels
# ax.set_xlabel('Quantity')
# ax.set_ylabel("Fruit")
# 
# # display chart inside the web page streamlitst.pyplot(fig)

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

fruits = {
    'Fruit': ['Apple', 'Orange', 'Banana', 'Melon', 'Strawberry'],
    'Value': [2.50, 4.00, 3.00, 5.50, 0.50],
    'Quantity': [10, 20, 30, 7, 99]
}

df = pd.DataFrame(fruits)

print(df['Fruit'].unique())
print(df['Value'].unique())
print(df['Quantity'].unique())

select_filters = st.selectbox("Select the Fruit", fruits['Fruit'])

filtered_df = df[df['Fruit'] == select_filters]

fig, ax = plt.subplots()
ax.plot(filtered_df['Fruit'],
        filtered_df['Value'])

ax.set_xlabel('Fruit')
ax.set_ylabel("Value")

st.pyplot(fig)



