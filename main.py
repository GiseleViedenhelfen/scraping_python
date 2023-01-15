import requests
from parsel import Selector
from pymongo import MongoClient


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError:
        return ''
    else:
        return response.text


def extract_books(book):
    selector = Selector(book)
    base_url = 'http://books.toscrape.com/catalogue/'
    booksInfo = []
    for item in selector.css('li.col-xs-6'):
        title = item.css('.product_pod h3 a::attr(title)').get()
        price = item.css('div p.price_color::text').re_first(r"£\d+\.\d{2}")
        detail_href = item.css("h3 a::attr(href)").get()
        detail_page_url = base_url + detail_href
        detail_response = fetch_content(detail_page_url)
        detail_selector = Selector(detail_response)
        description = (
            detail_selector.css("#product_description ~ p::text").get())
        booksInfo.append({
            "título": title,
            "preco": price,
            "descricao": description
            })
    return booksInfo


def pagination(url):
    next_page = 'page-1.html'
    all_books = []
    while next_page:
        print(next_page)
        content = fetch_content(url + next_page)
        all_books.extend(extract_books(content))
        next_page = Selector(content).css("li.next a::attr(href)").get()
    return all_books


url = 'http://books.toscrape.com/catalogue/'
call_scraping_function = pagination(url)

client = MongoClient("172.17.0.2:27017")
db = client.catalogue
book = call_scraping_function
db.books.insert_many(book)
print(book)
client.close()
