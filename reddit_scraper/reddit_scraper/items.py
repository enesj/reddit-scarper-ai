```python
import scrapy

class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    comments = scrapy.Field()
```