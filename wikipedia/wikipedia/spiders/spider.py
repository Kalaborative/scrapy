import scrapy
from wikipedia.items import WikipediaItem
from urlparse import urljoin


class MySpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org/"]
    start_urls = [
        'https://en.wikipedia.org/wiki/Category:2013_films',
    ]

    def parse(self, response):
        for title in response.xpath('//div[@id="mw-pages"]//li/a/text()').extract():
        	yield WikipediaItem(title=title)
        for title in response.xpath('//div[@id="mw-pages"]//li/a/@href').extract():
        	link = urljoin("http://en.wikipedia.org", title)
        	yield WikipediaItem(url=link)

        # yield item
        # items.append(item)
