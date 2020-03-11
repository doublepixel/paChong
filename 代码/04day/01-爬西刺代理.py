import urllib.request
import re
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context


class XiCiSpider():
    def __init__(self):
        self.url = 'https://www.xicidaili.com/nn/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }

        self.proxy_list = []

    def send_request(self, url):
        print(url)
        request = urllib.request.Request(url=url, headers=self.headers)
        response = urllib.request.urlopen(request)
        if response.status == 200:
            return response

    def parse_content(self, response):

        content = response.read().decode('utf8')
        pattern = re.compile(r'<td>(\d+\.\d+\.\d+\.\d+)</td>.*?<td>(\d+)</td>.*?<td>(H.*?)</td>', re.S)
        result = re.findall(pattern, content)

        for proxy in result:
            temp_proxy = {}
            temp_proxy['type'] = proxy[2]
            temp_proxy['proxy'] = proxy[0] + ":" + proxy[1]
            self.proxy_list.append(temp_proxy)

    def write_content(self):
        with open('proxy.json', 'w') as f:
            f.write(json.dumps(self.proxy_list))

    def satrt(self):
        for i in range(1, 5):
            full_url = self.url + str(i)
            response = self.send_request(full_url)
            if response:
                self.parse_content(response)

        self.write_content()


if __name__ == '__main__':
    xcs = XiCiSpider()
    xcs.satrt()
