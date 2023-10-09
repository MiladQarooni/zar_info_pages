import requests
from bs4 import BeautifulSoup
import pandas as pd

url_site = "https://zar.ir/p-41435/wedding-rings"

site = requests.get(url_site)

soup = BeautifulSoup(site.text, 'html.parser')

div1 = soup.find('div', {'id': 'product-summary-props'})

ul = div1.find('ul')
li_elements = ul.find_all('li')[:10]  # Get the first 10 li elements

data_dict = {}  # Initialize an empty dictionary to store data

for li in li_elements:
    spans = li.find_all('span')  # Find all spans within the current li element
    if len(spans) == 2:
        key = spans[0].text.strip()
        value = spans[1].text.strip()
        data_dict[key] = value

# for key, value in data_dict.items():
#     print(key,':',value)

df = pd.DataFrame([data_dict])
df.to_csv('data_dict.csv', index=False,encoding='UTF-16')



