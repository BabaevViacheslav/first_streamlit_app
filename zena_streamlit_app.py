import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('Zena Amazing Athleisure Catalog')



#Add button to load a list of colours
if streamlit.button('Get colour load list'):
  my_con = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  with my_con.cursor() as my_cur:
    my_cur.execute("select * from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")
    my_data_rows = my_cur.fetchall()
    streamlit.dataframe(my_data_rows).0

#for row in my_data_rows:
  #print("Colour: ", row[0])
  #print("\n")

