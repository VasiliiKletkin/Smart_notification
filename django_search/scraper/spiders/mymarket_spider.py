import json
from urllib.parse import unquote

import scrapy
from scrapy.http import JsonRequest
from tickets.models import Ticket

from ..items import AdScraperItem


class MyMarketSpider(scrapy.Spider):
    name = "MyMarket"

    def start_requests(self):
        if not self.start_urls and hasattr(self, "start_url"):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)"
            )
        data = {}
        for url in self.start_urls:
            yield JsonRequest(url=url, data=data)

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        items = jsonresponse["data"]["Prs"]
        for item in items:
            ad = AdScraperItem()
            ad["url"] = f'https://www.mymarket.ge/ru/pr/{item["product_id"]}'
            ad["title"] = item["title"]
            ad["ticket"] = Ticket.objects.get(url=unquote(response.url))
            yield ad
