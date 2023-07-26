from urllib.parse import unquote

import scrapy
from resources.models import Resource

from ..items import AdScraperItem


class SsSpider(scrapy.Spider):
    name = "Ss"

    resource = Resource.objects.get(name__icontains=name)
    start_urls = resource.tickets.filter(
        is_active=True).values_list("url", flat=True)

    def parse(self, response):
        hostname = response.url.split("://")[1].split("/")[0]
        items = response.css("div.latest_article_each")
        for item in items:
            ad = AdScraperItem()
            ad["url"] = unquote(
                hostname + item.css('div.latest_desc a').attrib["href"])
            ad["title"] = item.css("span.TiTleSpanList::text").get()
            ad.save()
            yield ad
