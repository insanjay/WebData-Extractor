from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

# Fetch the page
url = 'http://books.toscrape.com/'
page = requests.get(url)

# Parse the page content
soup = BeautifulSoup(page.text, 'html.parser')

# Find the desired elements
book_title = soup.find_all('h3')
book_price = soup.find_all('p', class_='price_color')
book_stock = soup.find_all('p', class_='instock availability')

# Clean prices
cleaned_prices = []
for pr in book_price:
    numeric_price = re.sub(r'[^\d.]', '', pr.text.strip())
    cleaned_prices.append(f'£{numeric_price}')  # Add the currency symbol back

# Collect data into a list of tuples
result = []
for t, pr, stock in zip(book_title, cleaned_prices, book_stock):
    result.append((t.text.strip(), pr, stock.text.strip()))

# Create the DataFrame
df = pd.DataFrame(result, columns=['Title', 'Price', 'Stock'])

# Save as CSV file in the same folder
df.to_csv('Books.csv', index=False, encoding='utf-8-sig')
print("CSV file created successfully in the current folder!")

# Save as JSON file in the same folder
df.to_json('Books.json', orient='records', lines=True, force_ascii=False)
print("JSON file created successfully in the current folder!")