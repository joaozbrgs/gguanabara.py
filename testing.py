import pandas as pd
import requests
from bs4 import BeautifulSoup

#Succesfully imported a wikipedia table:

def get_html_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_="data-table score")
    return pd.read_html(str(table.prettify()))[0]

url = 'https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/'
table_data = get_html_table(url)


def get_html_table2(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_="data-table name")
    return pd.read_html(str(table.prettify()))[0]

table_data = get_html_table(url)


name = get_html_table2(url=url)
score = get_html_table(url=url)

name = name.reset_index(axis=1)


df = name.merge(score, how='left', )

print(type(name))
# print(score)

print('\n')
#print((table_data))
print('\n')
