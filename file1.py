import streamlit

streamlit.title("MY PARENT MOM HEALTH DINNER")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry")
streamlit.text("Cake 3 & Spinach")
streamlit.text("Hord bolied eggs")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = streamlit.multiselect("Pick some Fruits :", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.Ioc[fruits_selected]
streamlit.dataframe(fruits_to_show)


