import urllib.request
import urllib.parse

import re

'''
https://www.neihan8.com/lxy//index.html
https://www.neihan8.com/lxy//index_2.html
https://www.neihan8.com/lxy//index_3.html
https://www.neihan8.com/lxy//index_4.html

'''


class NeiHanSpider():
    def __init__(self):
        self.page = 0
        self.url = 'https://www.neihan8.com/lxy//index'

    # 发送请求
    def send_request(self, url, page):
        print(url)
        response = urllib.request.urlopen(url)
        if response.status == 200:
            self.parse(response.read().decode('utf8'))
        else:
            print('出错了~')
            print(response.status)

    # 解析方法
    def parse(self, content):
        pattern = re.compile(r'.*?<div class="desc">(.*?)</div>', re.S)
        result = re.findall(pattern, content)
        result.pop(0)  # 处理无用数据
        for r in result:
            self.write_content(r)

    def write_content(self, content):
        with open('neihanba.txt', 'a', encoding='utf8') as f:
            f.write(content + '\n')

    def start(self):
        while True:
            self.page += 1
            if self.page == 1:
                self.send_request(self.url + '.html', self.page)
            else:
                full_url = self.url + '_' + str(self.page) + '.html'
                self.send_request(full_url, self.page)
            kw = input('任意键继续爬，按q退出')
            if kw == 'q':
                break


if __name__ == '__main__':
    nhs = NeiHanSpider()
    nhs.start()
