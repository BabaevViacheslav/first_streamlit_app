import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('Zena Amazing Athleisure Catalog')
streamlit.header('🍌🥭 Special Fruit Smoothie 🥝🍇')


#Add button to load a list of colours
if streamlit.button('Get colour load list'):
  my_con = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  with my_con.cursor() as my_cur:
    my_cur.execute("select COLOR_OR_STYLE from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")
    my_data_rows = my_cur.fetchall()
    streamlit.dataframe(my_data_rows)


streamlit.header('🍌🥭 Special Fruit Smoothie2 🥝🍇')


