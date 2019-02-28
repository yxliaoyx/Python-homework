from bs4 import BeautifulSoup
import requests
import numpy as np

url = 'https://data.gov.tw/news'
html = requests.get(url).content.decode('utf-8')
sp = BeautifulSoup(html, 'html.parser')
table = sp.find('table')

rows = table.find_all('tr')
title = [c.text for c in rows[0].find_all('th')]
data = [list() for _ in range(len(title))]

for r in rows[1:]:
    for col, cell_data in zip(data, r.find_all('td')):
        col.append(cell_data.text)

data_table = np.core.records.fromarrays(data)

for i in range(len(data_table)):
    print(data_table[i])
