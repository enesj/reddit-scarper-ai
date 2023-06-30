```python
import scrapy
from scrapy.crawler import CrawlerProcess
from web_scraper.spiders.reddit_spider import RedditSpider
from web_scraper.settings import SETTINGS

class RedditScraper:
    def __init__(self):
        self.process = CrawlerProcess(settings=SETTINGS)

    def run_spider(self):
        self.process.crawl(RedditSpider)
        self.process.start()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.run_spider()
```