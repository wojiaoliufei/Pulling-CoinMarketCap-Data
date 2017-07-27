import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

CMC_url = 'https://coinmarketcap.com/'
r = requests.get(CMC_url)
# print(r.text)

soup = BeautifulSoup(r.text, 'lxml')
table = soup.find('table')

dict1 = {'coin_position': [np.nan], 'coin_name': [np.nan], 'coin_marketcap': [np.nan], 'coin_price': [np.nan], 'coin_supply': [np.nan]}
coin_data = pd.DataFrame(dict1)

for row in table.find_all('tr')[1:]:
    col = row.find_all('td')

    coin_position = col[0].text.strip()
    coin_name = col[1].text.strip()
    coin_marketcap = col[2].text.strip()
    coin_price = col[3].text.strip()
    coin_supply = col[4].text.strip().split(" ")[0].rstrip()

    temp_df = {'coin_position': coin_position, 'coin_name': coin_name, 'coin_marketcap': coin_marketcap, 'coin_price': coin_price, 'coin_supply': coin_supply}

    coin_data = coin_data.append(temp_df, ignore_index=True)

coin_data = coin_data.drop(0)
print(coin_data)

#coin_data.to_csv('coinmarketcapdata.csv', index = False)
