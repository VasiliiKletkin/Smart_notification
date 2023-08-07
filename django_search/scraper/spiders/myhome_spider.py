from urllib.parse import unquote

import scrapy
from resources.models import Resource

from ..items import AdScraperItem


class MyHomeSpider(scrapy.Spider):
    name = "MyHome"
    resource = Resource.objects.get(name__icontains=name)
    tickets = resource.tickets.filter(is_active=True)
    iter_tickets = iter(tickets)
    start_urls = [ticket.url for ticket in tickets]

    def parse(self, response):
        current_ticket = next(self.iter_tickets)
        items = response.css("div.tatement-card")

        for item in items:
            ad = AdScraperItem()
            ad["url"] = unquote(item.css('a.card-container').attrib["href"])
            ad["title"] = item.css("h5.card-title::text").get()
            ad["ticket"] = current_ticket
            ad.save()
            yield ad
