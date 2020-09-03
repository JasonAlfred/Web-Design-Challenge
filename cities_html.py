import pandas as pd
import datetime

file = "resources/cities.csv"
cities_df = pd.read_csv(file)
cities_df.set_index('City_ID', inplace=True)
cities_df['City'] = cities_df['City'].str.title()

cities_df['Date'] = pd.to_datetime(cities_df['Date'],unit='s')
cities_df['Date'] = cities_df['Date'].dt.date

cities_html = cities_df.to_html()
html_file = open('data_page.html', 'w')
html_file = html_file.write(cities_html)
