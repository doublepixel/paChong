import urllib.request
import re
import ssl
import json
import random

ssl._create_default_https_context = ssl._create_unverified_context


class XiCiSpider():
    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }

        f = open('proxy.json', 'r')

        self.proxy_list = json.loads(f.read())  # 读数据

    def send_request(self, url):
        proxy = random.choice(self.proxy_list)

        proxy_use = {
            proxy['type']: proxy['proxy']
        }
        print(proxy_use)

        # 创建一个代理的handler
        proxyhandler = urllib.request.ProxyHandler(
            proxies=proxy_use
        )
        # 创建一个opener
        opener = urllib.request.build_opener(proxyhandler)

        # 创建一个request
        request = urllib.request.Request(url=url, headers=self.headers)

        # 发送请求
        response = opener.open(request)

        if response.status == 200:
            return response

    def satrt(self):
        for i in range(1, 5):
            full_url = self.url + str(i)
            response = self.send_request(full_url)
            print(response.read().decode('utf8'))


if __name__ == '__main__':
    xcs = XiCiSpider()
    xcs.satrt()
