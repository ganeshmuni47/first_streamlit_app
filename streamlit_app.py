import streamlit
streamlit.title('My Parents new healthy Dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled free-range egg')
streamlit.text('🥑 🍞 Avocado toast')

streamlit.header('🍌🥭Fruit Smoothie 🥝🍇')
streamlit.text('Oaty banana smoothie')
streamlit.text('Peachy oat smoothie')
streamlit.text('Strawberry banana smoothie')
streamlit.text('Blueberry lavender smoothie')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
##streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
