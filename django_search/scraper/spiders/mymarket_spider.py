import json

import scrapy
from resources.models import Resource
from scrapy.http import JsonRequest

from ..items import AdScraperItem


class MyMarketSpider(scrapy.Spider):
    name = "MyMarket"
    resource = Resource.objects.get(name__icontains=name)
    start_urls = resource.tickets.filter(is_active=True).values_list("url", flat=True)

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

        for item in jsonresponse["data"]["Prs"]:
            ad = AdScraperItem()
            ad["url"] = f'https://www.mymarket.ge/ru/pr/{item["product_id"]}'
            ad["title"] = item["title"]
            ad.save()
            yield ad
