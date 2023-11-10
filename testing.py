import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_html_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='wikitable')
    return pd.read_html(str(table.prettify()))[0]

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
table_data = get_html_table(url)

print(table_data)
