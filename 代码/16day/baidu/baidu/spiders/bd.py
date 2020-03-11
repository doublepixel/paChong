# -*- coding: utf-8 -*-
import scrapy


class BdSpider(scrapy.Spider):
    name = 'bd'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print('haha')
        print(response.request.headers)
        pass
