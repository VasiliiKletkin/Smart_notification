from scraper.spiders.myhome_spider import MyHomeSpider
from scraper.spiders.mymarket_spider import MyMarketSpider
from scraper.spiders.ss_spider import SsSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process

from django_search.celery import app

@app.task
def run_spiders():
    process = CrawlerProcess(get_project_settings())
    spiders = [MyMarketSpider, MyHomeSpider, SsSpider]
    
    for spider in spiders:
        process.crawl(spider)
    process.start()