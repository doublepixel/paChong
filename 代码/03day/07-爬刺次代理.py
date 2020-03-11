import urllib.request
import re
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context


class XiCiSpider():
    def __init__(self):
        self.authproxy = {
            "https": "496155678:tx4p1gbw@188.131.173.36:16816"
        }
        proxyhandler = urllib.request.ProxyHandler(
            proxies=self.authproxy
        )
        # 创建一个opener
        self.opener = urllib.request.build_opener(proxyhandler)

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        self.url = 'https://www.xicidaili.com/nn/2'

        self.iplist = []

    def send_request(self, url):
        request = urllib.request.Request(url, headers=self.headers)
        response = self.opener.open(request)
        if response.status == 200:
            return response

    def parse(self, response):
        content = response.read().decode()
        pattern = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>.*?<td>(\d+)</td>.*?<td>(H.*?)</td>', re.S)
        result = re.findall(pattern, content)

        for ip in result:
            dict = {}
            dict['type'] = ip[2]
            dict['ip'] = ip[0] + ":" + ip[1]
            self.iplist.append(dict)

    def write_content(self):
        with open('ip.json', 'w') as f:
            f.write(json.dumps(self.iplist))

    def start(self):
        response = self.send_request(self.url)
        self.parse(response)
        self.write_content()


if __name__ == '__main__':
    xcs = XiCiSpider()
    xcs.start()
