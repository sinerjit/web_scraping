import requests
import csv
import datetime
from bs4 import BeautifulSoup

def fetch_product_data(url, headers):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title_element = soup.find('h1', class_='product-single__title')
    title = title_element.get_text(strip=True)

    price_element = soup.find('span', class_='price-item price-item--regular')
    price = price_element.get_text(strip=True)

    today = datetime.date.today()
    return title, price, today

def save_to_csv(filename, data):
    header = ['Title', 'Price', 'Date']
    try:
        with open(filename, 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

if __name__ == "__main__":
    url = "https://smellofdubaisd.com/collections/arabian-desert/products/signature-oud-by-arabian-desert?variant=48193071513793"
    custom_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

    title, price, today = fetch_product_data(url, custom_headers)
    save_to_csv('WebScraperDataset.csv', [title, price, today])
