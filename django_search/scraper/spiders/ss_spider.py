from urllib.parse import unquote

import scrapy
from tickets.models import Ticket

from ..items import AdScraperItem


class SsSpider(scrapy.Spider):
    name = "Ss"

    def parse(self, response):
        hostname = response.url.split("://")[1].split("/")[0]
        items = response.css("div.latest_article_each")
        for item in items:
            ad = AdScraperItem()
            ad["url"] = unquote(
                hostname + item.css('div.latest_desc a').attrib["href"])
            ad["title"] = item.css("span.TiTleSpanList::text").get()
            ad["ticket"] = Ticket.objects.get(url=unquote(response.url))
            ad.save()
            yield ad
