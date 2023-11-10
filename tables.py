import math
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup



#73
def get_html_table(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_ = table)
    return pd.read_html(table.prettify())[0]

url = 'https://www.google.com/search?q=tabela+brasileirao&rlz=1C1GCEU_pt-BRBR1044BR1044&oq=tabela+brasileirao&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQABgDMgYIAhAAGAMyBggDEAAYAzINCAQQABiDARixAxiABDIHCAUQABiABDIGCAYQABgDMgYIBxAAGAMyBggIEAAYAzIGCAkQABgD0gEINTY1OGoxajeoAgCwAgA&sourceid=chrome&ie=UTF-8#sie=lg;/g/11jspy1hvm;2;/m/0fnk7q;st;fp;1;;;'
table_data = get_html_table(url)

print(table_data)

