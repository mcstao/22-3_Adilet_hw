
import requests
from bs4 import BeautifulSoup as BS


URL = "https://nitecore.ua/ua/category/nalobnie-fonari/"

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="col-md-3 col-sm-6 col-6 product-card-wrapper")
    fonar = []
    for item in items:
        fonar.append({
            "title": item.find("div", class_="product-title").find("a").getText(),
            "price": item.find("div", class_="d-flex justify-content-center w-100").getText(),
            "link": item.find("a").get("href")
        })
    return fonar

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        fonar = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data(html.text)
            fonar.extend(current_page)
        return fonar
    else:
        raise Exception("Error in parser!")


