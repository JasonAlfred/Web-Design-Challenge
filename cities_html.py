import pandas as pd

file = "resources/cities.csv"
cities_df = pd.read_csv(file)
cities_df.set_index('City_ID', inplace=True)
cities_html = cities_df.to_html()
html_file = open('data_page.html', 'w')
html_file = html_file.write(cities_html)
