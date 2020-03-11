# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# 深度爬虫
class XcfSpider(CrawlSpider):
    name = 'xcf'
    allowed_domains = ['xiachufang.com']
    start_urls = ['http://www.xiachufang.com/category/40076/']

    rules = (
        Rule(LinkExtractor(allow=r'/category/\d+/')),
        Rule(LinkExtractor(allow=r'/recipe/\d+/'), callback='parse_item', follow=False, process_links='check_links'),
    )

    def check_links(self, links):
        # print(links)
        return links


    def parse_item(self, response):
        title = response.css('h1::text').extract_first()
        print(title)
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
