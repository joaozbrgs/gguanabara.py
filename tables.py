import pandas as pd
import requests
from bs4 import BeautifulSoup

#Attempt to import a wikipedia table:

# def get_html_table(url):
#     response1 = requests.get(url)
#     soup1 = BeautifulSoup(response1.content, 'html.parser')
#     table1 = soup1.find('table', class_='wikitable')
#     return pd.read_html(str(table1.prettify()))[0]

# url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
# table_data1 = get_html_table(url)

# print(table_data1) #Success

#Attempt to import a soccer league table

def get_html_table(url):
    response2 = requests.get(url)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    table2 = soup2.find('a', title_ ="Colunas")#class_ = 'data-table score')
    return pd.read_html(str(table2))[0] #pd.read_html(str(table2.prettify()))[0]

url = 'https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/'
table_data2 = get_html_table(url)

print((table_data2)) #Success



