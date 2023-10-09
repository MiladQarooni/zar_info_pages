import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize empty lists to store data
all_prices = []
all_names = []
all_models = []

# Define the base URL and the total number of pages to scrape
base_url = "https://zar.ir/shop/cat-2663-{}.html"
total_pages = 6  # Set the total number of pages to scrape

for page_number in range(1, total_pages + 1):
    url_site = base_url.format(page_number)
    site = requests.get(url_site)

    if site.status_code != 200:
        break

    soup = BeautifulSoup(site.text, 'html.parser')
    div1 = soup.find('div', {'class': 'grid-container'})
    div2 = div1.find_all('div', {'class': 'Box'})

    prices = []
    names = []
    models = []

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

    #Extend the master lists with data from the current page
    all_prices.extend(prices)
    all_names.extend(names)
    all_models.extend(models)

# Create the DataFrame after scraping all pages
zarDictionary = {
    'price': all_prices,
    'namee': all_names,
    'model': all_models
}





df = pd.DataFrame(zarDictionary)
df.to_csv('zarDictionary.csv', index=False,encoding='UTF-16')
