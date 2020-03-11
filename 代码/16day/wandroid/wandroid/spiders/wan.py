# -*- coding: utf-8 -*-
import scrapy


class WanSpider(scrapy.Spider):
    name = 'wan'
    allowed_domains = ['wanandroid.com']

    login_url = 'https://wanandroid.com/user/login'
    collection_url = 'https://wanandroid.com/lg/collect'
    start_urls = ['http://wanandroid.com/']

    def start_requests(self):
        form_data = {
            'username': '496155678@qq.com',
            'password': '123456'
        }

        yield scrapy.FormRequest(url=self.login_url, formdata=form_data, method='POST', callback=self.parse)

    # 登录成功
    def parse(self, response):
        # print(response.cookies)
        yield scrapy.Request(url=self.collection_url, callback=self.collection)

    def collection(self, response):
        print(response.request.headers)
        with open('wan.html', 'w') as f:
            f.write(response.text)
