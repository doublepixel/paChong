import requests
import json
import time


class ShuCaiSpider():
    def __init__(self):
        self.url = 'http://www.cncyms.cn/pages.php'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }
        self.i_time = None

        self.pgnum = 0

    def send_request(self, form_data):
        response = requests.post(url=self.url, data=form_data)
        if response.status_code == 200:
            return response

    def parse_content(self, response):
        print('正在爬%d' % self.pgnum)
        json_content = response.json()
        for result in json_content.get('list'):
            releasetime = result.get('ReleaseTime')
            time_c = self.get_time(releasetime)  # 数据的时间
            if time_c < self.i_time:
                return

        self.write_content(json_content)
        self.pgnum += 1
        form_data = {
            'pageNum': self.pgnum,
            'pname': self.name,
            'reltime': '蔬菜'
        }
        response = self.send_request(form_data)
        if response:
            self.parse_content(response)

    def write_content(self, json_content):
        with open('shucai.json', 'w') as f:
            f.write(json.dumps(json_content, ensure_ascii=False))

    def start(self):
        self.name = input('请输入你要爬取的蔬菜名字（如果输入全部就是爬全部）:')
        time = input('请输入你要爬取到指定日期(2019-10-11):')
        self.i_time = self.get_time(time)

        if self.name == '全部':
            self.name = ''

        form_data = {
            'pageNum': self.pgnum,
            'pname': self.name,
            'reltime': '蔬菜'
        }
        response = self.send_request(form_data)
        if response:
            self.parse_content(response)

    def get_time(self, t):
        ft = '%Y-%m-%d'
        strp_time = time.strptime(t, ft)
        time_c = time.mktime(strp_time)
        return time_c


if __name__ == '__main__':
    scs = ShuCaiSpider()
    scs.start()
