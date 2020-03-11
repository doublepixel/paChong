# -*- coding: utf-8 -*-
import scrapy
from joke.items import JokeItem


class JkSpider(scrapy.Spider):
    name = 'jk'
    allowed_domains = ['biedoul.com']
    page = 1
    base_url = 'https://www.biedoul.com/index/'
    start_urls = [base_url + str(page) + "/"]

    def parse(self, response):
        dl_list = response.xpath('//dl[@class="xhlist"]')
        for dl in dl_list:
            try:
                content = "".join(dl.xpath('.//font//text()').extract())
                item = JokeItem()
                item['content'] = content
                yield item
            except Exception as e:
                print('出现异常了')
        if self.page < 100:
            self.page += 1
            next_url = self.base_url + str(self.page) + "/"
            yield scrapy.Request(next_url, callback=self.parse)
