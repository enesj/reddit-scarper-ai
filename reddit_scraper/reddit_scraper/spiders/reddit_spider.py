```python
import scrapy
from reddit_scraper.items import ScraperItem

class RedditSpider(scrapy.Spider):
    name = 'reddit_spider'
    start_urls = ['http://www.reddit.com']

    def parse(self, response):
        for post in response.css('div.thing'):
            item = ScraperItem()
            item['title'] = post.css('p.title a::text').get()
            item['url'] = post.css('p.title a::attr(href)').get()
            item['upvotes'] = post.css('div.score.unvoted::attr(title)').get()
            yield item

        next_page = response.css('span.next-button a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```