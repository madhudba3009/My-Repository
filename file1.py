import streamlit

streamlit.title("MY PARENT MOM HEALTH DINNER")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry")
streamlit.text("Cake 3 & Spinach")
streamlit.text("Hord bolied eggs")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streanlit.dataframe(my_fruit_list)
