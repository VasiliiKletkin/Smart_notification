from urllib.parse import unquote

import scrapy
from resources.models import Resource

from ..items import AdScraperItem


class MyHomeSpider(scrapy.Spider):
    name = "MyHome"

    resource = Resource.objects.get(name__icontains=name)
    start_urls = resource.tickets.filter(
        is_active=True).values_list("url", flat=True)

    def parse(self, response):
        items = response.css("div.tatement-card")

        for item in items:
            ad = AdScraperItem()
            ad["url"] = unquote(item.css('a.card-container').attrib["href"])
            ad["title"] = item.css("h5.card-title::text").get()
            ad.save()
            yield ad
