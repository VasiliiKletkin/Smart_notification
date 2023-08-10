from resources.models import Resource
from scraper.spiders.myhome_spider import MyHomeSpider
from scraper.spiders.mymarket_spider import MyMarketSpider
from scraper.spiders.ss_spider import SsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from django_search.celery import app


@app.task
def run_spiders():
    process = CrawlerProcess(get_project_settings())
    spiders = [MyMarketSpider, MyHomeSpider, SsSpider]

    for spider in spiders:
        resource = Resource.objects.get(name__icontains=spider.name)
        if tickets:= resource.tickets.filter(is_active=True):
            start_urls = [ticket.url for ticket in tickets]
            process.crawl(spider, start_urls=start_urls)
    process.start()
