import requests
from lxml import etree
import os


class DouTuLaSpider():
    def __init__(self):
        self.url = 'https://www.doutula.com/article/list/?page='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }

    # 发送请求
    def send_request(self, url):
        print(url)
        response = requests.get(url=url, headers=self.headers)
        return response

    def parse_content(self, response):
        html = response.text
        content = etree.HTML(html)
        a_list = content.xpath('//div[@class="col-sm-9 center-wrap"]//a')
        print(a_list)
        for a in a_list:
            title = a.xpath('./div[@class="random_title"]/text()')  # xpath取出来的是列表
            pic_list = a.xpath('.//div[@class="random_article"]//img/@jiayuan-original')
            if title:
                if not os.path.exists('doutu/' + title[0]):
                    os.mkdir('doutu/' + title[0])
                for index, pic in enumerate(pic_list):
                    response = self.send_request(pic)  # 发送图片请求
                    name = str(index + 1) + "_" + pic[-20:]  # 图片名字
                    self.write_content(response, name, 'doutu/' + title[0])

    '''
    http://ww3.sinaimg.cn/bmiddle/9150e4e5ly1fmg8ko8r5jg206o06o0sr.gif
    '''

    def write_content(self, response, name, path):
        print('正在写入%s' % name)
        with open(path + '/' + name, 'wb') as f:
            f.write(response.content)

    def start(self):
        for i in range(1, 2):
            full_url = self.url + str(i)
            reponse = self.send_request(full_url)
            self.parse_content(reponse)


if __name__ == '__main__':
    dtl = DouTuLaSpider()
    dtl.start()
