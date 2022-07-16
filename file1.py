import streamlit

streamlit.title("MY PARENT MOM HEALTH DINNER")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry")
streamlit.text("Cake 3 & Spinach")
streamlit.text("Hord bolied eggs")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some Fruits :", list(my_fruit_list.index),['Avocado','Strawberries'])
streamlit.dataframe(my_fruit_list)

