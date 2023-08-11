import streamlit
import pandas as pd


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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])  #using index lets you pick the fruit by index?
#filter dataframe rows by fruit index
fruits_to_show = my_fruit_list.loc[fruits_selected


#display the table on the page
streamlit.dataframe(fruits_to_show)
