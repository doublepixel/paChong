# -*- coding: utf-8 -*-
import scrapy
import re
from lxml import etree
from bs4 import BeautifulSoup
from paowangrizi.items import PaowangriziItem


class PwSpider(scrapy.Spider):
    name = 'pw'
    allowed_domains = ['jcodecraeer.com']
    base_url = 'http://www.jcodecraeer.com'
    start_urls = ['http://www.jcodecraeer.com/plus/list_tid_4.html']

    def parse(self, response):
        '''
        1、正则
        2、xpath
        3、bs4
        :param response:
        :return:
        '''
        # re.match(r'\d',response.text)

        # html = etree.HTML(response.text)
        # html.xpath('//div')

        # soup = BeautifulSoup(response.text,'lxml')
        # soup.select('h3')

        li_list = response.css('.archive-list>li')
        # print(len(li_list))
        for li in li_list:
            title = li.css('h3>a::text').extract_first()
            href = li.css('h3>a::attr(href)').extract_first()
            detail = li.xpath('.//div[@class="archive-detail"]/p/text()').extract_first()
            author = li.xpath('.//li[@class="list-user"]//span/text()').extract_first()
            vnum = li.xpath('.//li[@class="list-msg"]//span[@class="glyphicon-class"][1]/text()').extract_first()
            cnum = li.xpath('.//li[@class="list-msg"]//span[@class="glyphicon-class"][2]/text()').extract_first()
            time = li.xpath('.//div[@class="archive-data"]//span//text()').extract_first()
            full_url = self.base_url + href[2:]

            item = PaowangriziItem()
            item['title'] = title
            item['full_url'] = full_url
            item['detail'] = detail
            item['author'] = author
            item['vnum'] = vnum
            item['cnum'] = cnum
            item['time'] = time
            yield scrapy.Request(url=full_url, callback=self.parse_content, meta={"item": item})

    def parse_content(self, response):
        item = response.meta.get('item')
        content = "".join(response.xpath('//div[@class="arc_body"]//text()').extract())
        item['content'] = content
        yield item
