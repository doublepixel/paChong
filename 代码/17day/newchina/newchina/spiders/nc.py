# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class NcSpider(RedisCrawlSpider):
    name = 'nc'
    allowed_domains = ['china.com']
    # start_urls = ['https://tech.china.com/']
    redis_key = 'china:start_urls'
    rules = (
        Rule(LinkExtractor(allow=r'/article/.*?.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        title = response.css('h1::text').extract_first()
        item['title'] = title
        print(title)
        yield item
