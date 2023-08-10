from urllib.parse import unquote

import scrapy
from tickets.models import Ticket

from ..items import AdScraperItem


class MyHomeSpider(scrapy.Spider):
    name = "MyHome"

    def parse(self, response):
        items = response.css("div.tatement-card")
        for item in items:
            ad = AdScraperItem()
            ad["url"] = unquote(item.css('a.card-container').attrib["href"])
            ad["title"] = item.css("h5.card-title::text").get()
            ad["ticket"] = Ticket.objects.get(url=unquote(response.url))
            ad.save()
            yield ad
