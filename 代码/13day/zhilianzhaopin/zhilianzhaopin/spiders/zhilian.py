# -*- coding: utf-8 -*-
import scrapy
import json
from zhilianzhaopin.items import ZhilianzhaopinItem


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'  # 爬虫名字
    allowed_domains = ['zhaopin.com']  # 允许爬的于
    start = 0

    url = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3'

    start_urls = [url.format(start)]  # 起始

    # 解析数据的地方
    def parse(self, response):
        # response.text相当于requests.text
        # response.body相当于requests.content
        print(response.text)
        dict_result = json.loads(response.text)
        results = dict_result['data']['results']
        for res in results:
            jobName = res['jobName']
            salary = res['salary']
            eduLevel = res['eduLevel']['name']
            # 把数据给item对象
            item = ZhilianzhaopinItem()
            item['jobName'] = jobName
            item['salary'] = salary
            item['eduLevel'] = eduLevel
            yield item
        # 发起下一页请求
        if self.start < 450:
            self.start += 90

            url = self.url.format(self.start)
            yield scrapy.Request(url=url, callback=self.parse)
