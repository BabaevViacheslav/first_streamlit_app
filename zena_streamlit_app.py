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
    my_cur.execute("select color_or_style, price, direct_url,size_list,upsell_product_desc   from ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")
    my_data_rows = my_cur.fetchall()
    df = pandas.DataFrame(my_data_rows)
    streamlit.write(df[2])

#for row in my_data_rows:
  #print("Colour: ", row[0])
  #print("\n")

