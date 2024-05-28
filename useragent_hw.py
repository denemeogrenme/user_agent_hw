import requests

from bs4 import BeautifulSoup

import pandas as pd

url = "http://books.toscrape.com/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

books = []

for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    books.append([title, price, availability])

df = pd.DataFrame(books, columns=['Title', 'Price', 'Availability'])

df.to_csv('books.csv', index=False)

print("Veriler CSV dosyasına kaydedildi.")
