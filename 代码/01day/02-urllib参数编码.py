import urllib.request
import urllib.parse

# kw = {'kw': '美女'}
#
# result = urllib.parse.urlencode(kw)
# print(result)

# re = urllib.parse.unquote(result)
# print(re)

# url = 'https://tieba.baidu.com/f?'
#
# full_url = url + result
# response = urllib.request.urlopen(full_url)
# print(response.read())

'''
取前10页、把页面的数据保存到本地、用面向对象写

'''


class TieBaSpider():
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?'

    def send_request(self, url, page):
        print('正在发送第{}页'.format(page))
        response = urllib.request.urlopen(url)
        self.write_file(response.read(), page)

    def write_file(self, content, page):
        print('正在保存第{}页'.format(page))
        with open('tieba_{}.html'.format(page), 'wb') as f:
            f.write(content)

    def start(self):
        page = int(input('请输入你要爬取的页数'))
        for i in range(1, page + 1):
            # https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&pn=0
            pn = (i - 1) * 50
            kw = {'kw': '美女', 'pn': pn}
            result = urllib.parse.urlencode(kw)
            full_url = self.url + result
            self.send_request(full_url, i)


if __name__ == '__main__':
    tbs = TieBaSpider()
    tbs.start()
