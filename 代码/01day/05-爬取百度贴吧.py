import urllib.parse
import urllib.request
import re
import os


class TieBaSpider():
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?'
        self.turl = 'https://tieba.baidu.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }

    def send_request(self, url):
        # 第一步构造request
        request = urllib.request.Request(url=url, headers=self.headers)

        # 发送请求
        response = urllib.request.urlopen(request)

        if response.status == 200:
            content = response.read()
            return content
        else:
            print('出错了~', response.status)

    def parse_detail(self, content):
        pattern = re.compile(r'<img.*?class="BDE_Image".*?src="(.*?)".*?>', re.S)
        pic_list = re.findall(pattern, content)
        for pic in pic_list:
            content = self.send_request(pic)  # 发送图片请求
            name = pic[-20:]
            self.write_content(content, name)

    def parse(self, content):
        pattern = re.compile(r'<a\srel="noreferrer"\shref="(/p/.*?)".*?</a>', re.S)
        link_list = re.findall(pattern, content)

        for link in link_list:
            detail_url = self.turl + link
            print(detail_url)
            content = self.send_request(detail_url).decode('utf8')
            self.parse_detail(content)

    def write_content(self, content, name):
        print('正在存在%s' % name)
        path = 'tieba'
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + '/' + name, 'wb') as f:
            f.write(content)

    def write_html(self, content):
        with open('tieba.html', 'wb') as f:
            f.write(content)

    '''
    https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&pn=100
    '''

    def start(self):
        kw = input('请输入爬取的贴吧名字')
        page = int(input('请输入你爬取多少页'))  # 5
        for i in range(1, page + 1):
            pn = (i - 1) * 50
            keyword = {'kw': kw, 'pn': pn}
            result = urllib.parse.urlencode(keyword)
            # print(result)
            full_url = self.url + result
            # print(full_url)
            content = self.send_request(full_url).decode('utf8')
            self.parse(content)  # 提取/p/123123312312


if __name__ == '__main__':
    tbs = TieBaSpider()
    tbs.start()
