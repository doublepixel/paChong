import requests
from lxml import etree
import urllib.parse
import os
import time


class ZuoWenSpider():
    def __init__(self):
        self.url = 'https://www.99zuowen.com/xiaoxuezuowen/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        self.base_dir = '作文'
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)

    # 发送请求
    def send_request(self, url):
        print(url)
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response
        else:
            print(response.status_code)

    # 解析分类
    def parse_content(self, response):
        html = etree.HTML(response.text)
        a_list = html.xpath(
            '//div[@class="main_box main_chuyi clearfix"]/div[@class="col260"]/dl[@class="type_list2"][1]//dd//a')
        for a in a_list:
            name = a.xpath('./text()')[0]
            href = a.xpath('./@href')[0]
            full_url = urllib.parse.urljoin(self.url, href)
            # print(full_url)

            if not os.path.exists(self.base_dir + "/" + name):
                os.mkdir(self.base_dir + "/" + name)

            response = self.send_request(full_url)  # 列表页请求
            if response:
                self.parse_list(response, name, response.url)

    # 解析列表
    def parse_list(self, response, name, c_url):
        html = etree.HTML(response.text)
        li_list = html.xpath('//li[@class="lis"]')

        for li in li_list:
            time.sleep(0.5)
            href = li.xpath('./h4/a/@href')[0]
            response = self.send_request(href)  # 具体页请求
            if response:
                self.parse_detail(response, name)
        # 解析下一页
        next_list = html.xpath('//div[@class="page"]//li[last()-1]/a/@href')
        if next_list:
            next = next_list[0]
            response = self.send_request(c_url + next)
            if response:
                self.parse_list(response, name, c_url)

    # 解析内容
    def parse_detail(self, response, name):
        html = etree.HTML(response.text)
        title = html.xpath('//h1/text()')[0]
        content = "".join(html.xpath('//div[@class="content"]//p//text()'))
        self.write_content(self.base_dir + '/' + name + "/" + title + ".txt", content)

    # 写入文件
    def write_content(self, path, content):
        # 作文/写人/我亲爱的李老师.txt
        with open(path, 'w') as f:
            f.write(content)

    def start(self):
        response = self.send_request(self.url)
        if response:
            self.parse_content(response)


if __name__ == '__main__':
    zws = ZuoWenSpider()
    zws.start()
