# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZuhaoSpider(CrawlSpider):
    name = 'zuhao'
    allowed_domains = ['zuhaowan.com']
    start_urls = ['https://www.zuhaowan.com/zuhao-17/']
    # 没有callback follow默认true
    rules = (
        Rule(LinkExtractor(allow=r'/zuhao-17/\d+.html'), process_links='check_links'),
        Rule(LinkExtractor(allow=r'/zuhao/\d{7}.html'), process_links='check_detail_links', follow=False,
             callback='parse_item'),
    )

    def check_links(self, links):
        # print(links)
        return links

    def check_detail_links(self, links):
        # print(links)
        return links

    '''
    这里面千万不能parse方法
    '''

    def parse_item(self, response):
        title = response.xpath('//div[@class="info-title"]/text()').extract_first()
        print(title)

        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
