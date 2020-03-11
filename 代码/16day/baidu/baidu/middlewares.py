# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class BaiduSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class BaiduDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


import random
import base64


# UA池中间件
class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agents = spider.settings['USER_AGENTS']
        ua = random.choice(user_agents)
        print(ua)
        request.headers['User-Agent'] = ua
        return None


# 代理中间件
class ProxyMiddlewares(object):
    def process_request(self, request, spider):
        proxies = spider.settings['PROXIES']
        proxy = random.choice(proxies)
        print(proxy)
        if proxy['user_pwd'] is None:
            # 没有代理账户验证的代理使用方式
            if proxy['type'] == 'HTTP':
                # http://128.28.29.01:8888
                u = "http://%s" % proxy['ip_port']
                request.meta['proxy'] = u
            else:
                # https://128.28.29.01:8888
                u = "https://%s" % proxy['ip_port']
                request.meta['proxy'] = u
            print(u)
        else:
            # 对账户密码进行base64编码
            user_pwd = base64.b64encode(proxy['user_pwd'].encode('utf-8')).decode('utf-8')
            # 对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + user_pwd
            request.meta['proxy'] = "https://%s" % proxy['ip_port']


class RandomCookiesMiddleware(object):

    def process_request(self, request, spider):
        cookies = spider.settings['COOKIES']
        # 随机获取一个cookies
        cookie = random.choice(cookies)
        print(cookie)
        if cookie:
            request.cookies = cookie


from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from scrapy.http import HtmlResponse
import time
class SeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/Users/xiaoyuan/Downloads/chromedriver')
        self.driver.set_page_load_timeout(10)

    def process_request(self, request, spider):
        try:
            url = request.url
            self.driver.get(url)

            input = self.driver.find_element_by_id('kw')
            time.sleep(1)
            input.send_keys('美女')
            time.sleep(1)
            btn = self.driver.find_element_by_id('su')
            btn.click()
            time.sleep(3)
            self.driver.save_screenshot('baidu.png')
            btn = self.driver.find_element_by_class_name('n')
            btn.click()
            if self.driver.page_source:
                return HtmlResponse(url=url, body=self.driver.page_source, status=200, encoding='utf-8',
                                    request=request)
        except TimeoutException:
            print('请求超时')
            return HtmlResponse(url=request.url, body=None, status=500)