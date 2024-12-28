import time
from scraper import fetch_product_data, save_to_csv
from email_notifier import send_mail

def check_price():
    url = "https://smellofdubaisd.com/collections/arabian-desert/products/signature-oud-by-arabian-desert?variant=48193071513793"
    custom_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"}

    title, price, today = fetch_product_data(url, custom_headers)
    save_to_csv('WebScraperDataset.csv', [title, price, today])

    # Check price and send an email if it meets certain conditions
    # Example condition: if price is below a certain amount
    # if float(price.replace('$', '')) < 15:
    #     send_mail('sarp.cubukcuoglu@gmail.com', 'AlexTheAnalyst95@gmail.com', 'Price Alert!', 'The price has dropped below $15!', 'xxxxxxxxxxxxxx')

if __name__ == "__main__":
    while True:
        check_price()
        time.sleep(86400)  # Sleep for 24 hours
