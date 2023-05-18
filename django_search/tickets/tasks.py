import requests
from ads.models import Ad
from bs4 import BeautifulSoup

from django_search.celery import app

from .models import Ticket


@app.task
def get_ads(url):
    response = requests.get(url)
    hostname = response.url.split("://")[1].split("/")[0]
    soup = BeautifulSoup(response.text, "html.parser")
    ads = []
    if hostname == "ss.ge":
        items = soup.find_all("div", class_="latest_article_each")
        for item in items:
            price = item.find("div", class_="latest_price").get_text()
            title = item.find("span", class_="TiTleSpanList").get_text()
            url = item.find("a").get("href")

            ad = {
                "title": title,
                "price": price,
                "url": hostname + url,
            }
            ads.append(ad)
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
