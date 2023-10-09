import requests
from bs4 import BeautifulSoup
import pandas as pd

url_site = "https://zar.ir/shop/cat-2663-1.html"

site = requests.get(url_site)

soup = BeautifulSoup(site.text, 'html.parser')

div1 = soup.find('div' , {'class': 'grid-container'})

div2 = div1.find_all('div', {'class': 'Box'})

prices = []
names = []
models = []

zarDictionary = {
    'price': prices,
    'namee': names,
    'model': models
}
# # #
for item in range(len(div2)):
    price_element = div2[item].find('div', {'class': 'lblprice'})
    if price_element:
        price_text = price_element.text.strip()
        if price_text == 'تماس بگیرید':
            prices.append('تماس بگیرید')
        else:
            price = int(price_text.replace(',', '').replace('تومان', ''))
            prices.append(price)
    else:
        prices.append(None)

    title_element = div2[item].find('span')
    if title_element:
        title_text = title_element.text.strip()
        name = title_text[:-7]
        model = title_text[-7:]
        names.append(name)
        models.append(model)
    else:
        names.append(None)
        models.append(None)

df = pd.DataFrame(zarDictionary)
df.to_csv('zarDictionary.csv')



