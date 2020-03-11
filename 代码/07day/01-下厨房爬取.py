import requests
import urllib.parse
from lxml import etree
import csv


class XiaChuFangSpider():
    def __init__(self):
        self.url = 'http://www.xiachufang.com/category/40076/?page='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        f = open('caipu.csv', 'a')
        fieldnames = ['name', 'stats', 'desc', 'all_zl', 'step']
        self.writer = csv.DictWriter(f, fieldnames)
        self.writer.writeheader()

    # 发送请求
    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response

    def parse_content(self, response):
        html = etree.HTML(response.content)  # 小问题
        li_list = html.xpath('//ul[@class="list"]//li')
        for li in li_list:
            name = li.xpath('.//p[@class="name"]/a/text()')[0]
            href = li.xpath('.//p[@class="name"]/a/@href')[0]
            stats = li.xpath('.//p[@class="stats"]/span[1]/text()')[0]

            detail_url = urllib.parse.urljoin(self.url, href)

            dict_greens = {
                'name': name,
                'stats': stats,
            }
            self.parse_detail(detail_url, dict_greens)

    def parse_detail(self, detail_url, dict_greens):
        response = self.send_request(detail_url)
        if response:
            html = etree.HTML(response.content)
            desc = "".join(html.xpath('//div[@class="desc mt30"]//text()'))
            tr_list = html.xpath("//tr[contains(@itemprop,'recipeIngredient')]")
            print(tr_list)
            all_zl = ''
            for tr in tr_list:
                zl = tr.xpath('./td//text()')
                all_zl += "".join(zl)
                all_zl += ","
            all_zl = all_zl.replace('\n', "").replace(" ", "").rsplit(',', 1)[0]
            step = html.xpath("//li[contains(@class,'container')]//text()")
            step = "".join(step)
            dict_greens['all_zl'] = all_zl
            dict_greens['step'] = step
            dict_greens['desc'] = desc
            self.write_content(dict_greens)

    def write_content(self, content):
        self.writer.writerow(content)

    def start(self):
        for i in range(1, 10):
            full_url = self.url + str(i)
            print(full_url)
            response = self.send_request(full_url)
            if response:
                self.parse_content(response)


if __name__ == '__main__':
    xcfs = XiaChuFangSpider()
    xcfs.start()
