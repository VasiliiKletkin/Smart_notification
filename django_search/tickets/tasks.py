from urllib.parse import unquote

import requests
from ads.models import Ad
from bs4 import BeautifulSoup

from django_search.celery import app

from .models import Ticket


@app.task
def get_ads(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
    response = requests.get(url, headers=headers)
    hostname = response.url.split("://")[1].split("/")[0]
    soup = BeautifulSoup(response.text, "html.parser")
    ads = []
    if not response.status_code:
        print("ERROR")
        return []
    
    if hostname == "ss.ge":
        items = soup.find_all("div", class_="latest_article_each")
        for item in items:
            try:
                title = item.find("span", class_="TiTleSpanList").get_text()
                price = item.find("div", class_="latest_price").get_text()
                url = item.find("a").get("href")
                ad = {"title": title,"price": price,"url": unquote(hostname + url)}
                ads.append(ad)
            except:
                continue

    elif hostname == "www.myhome.ge":
        items = soup.find_all("div", class_="statement-card")
        for item in items:
            try:
                title = item.find("h5", class_="card-title").get_text()
                price = item.find("b", class_="item-price-usd").get_text()
                url = item.find("a", class_="card-container").get("href")
                ad = {"title": title,"price": price,"url": unquote(url)}
                ads.append(ad)
            except:
                continue
    return ads


@app.task
def parse_ticket(id):
    ticket = Ticket.objects.get(id=id)
    print("START PARSE: " + ticket.url)
    ads = get_ads(ticket.url)
    count_old = ticket.ads.count()
    for ad in ads:
        try:
            Ad.objects.create(
                ticket=ticket,
                url=ad["url"],
                title=ad["title"],
                price=ad["price"],
            )
        except Exception as e:
            continue
    count_add = ticket.ads.count() - count_old
    print("END PARSE: " + ticket.url + " ADD " + str(count_add))


@app.task
def parse_data():
    tickets = Ticket.objects.filter(is_active=True)
    for ticket in tickets:
        parse_ticket.delay(ticket.id)
