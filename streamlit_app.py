import streamlit
import pandas as pd
import requests

#page header
streamlit.title("My Mom's New Healthy Diner")

#breakfast menu.  header and menu items.
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

#second header banner for smoothies promotion
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#read fruit dataset and display
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#set my_fruit_list index to the fruit name
my_fruit_list = my_fruit_list.set_index("Fruit")

#add Multi-select widget to pandas dataset
#setting 'Avocado' and 'Strawberries' as default selection
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])  #using index lets you pick the fruit by index?
#filter dataframe rows by fruit index
fruits_to_show = my_fruit_list.loc[fruits_selected]


#display the table on the page
streamlit.dataframe(fruits_to_show)

#header for Fruityvice section.
streamlit.header('Fruityvice Fruit Advice!')
#api request for fruityvice data
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

streamlit.text(fruityvice_response.json())  #just writes the json to the screen

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output normalized json to screen as a table
streamlit.dataframe(fruityvice_normalized)


