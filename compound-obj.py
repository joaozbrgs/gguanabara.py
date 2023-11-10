import pandas as pd
import requests
from bs4 import BeautifulSoup

#Tuples

#72
t1=(
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten'
)

print("=" * 100)
print('Now you will type a number from 0 to 10 and it will display it on text format')
print("=" * 100)

a1 = input('\nType your number between 0 and 10: ')
while True:
    try:
        a1 = int(a1)
        if a1 in range(0,11):
            break
        else:
            a1 = int(input('Your number was out of range. Type a new one: '))
    except ValueError:
        a1 = int(input('type a valid answer: '))


print(f'You typed the number {t1[a1]}!')



#73
def get_html_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')
    return pd.read_html(str(table.prettify()))[0]

url = 'https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/'
table_data = get_html_table(url)

print(table_data[0])
