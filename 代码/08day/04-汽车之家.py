import requests
from bs4 import BeautifulSoup
import json
import csv
import re


class QiCheSpider():
    def __init__(self):
        self.url = 'https://www.autohome.com.cn/all/%s/#liststart'
        self.c_url = 'https://reply.autohome.com.cn/api/getData_ReplyCounts.ashx'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        }
        # 写入csv
        csv_f = open('car.csv', 'a', encoding='utf-8-sig')
        fieldnames = ['title', 'content', 'time', 'vnum', 'cnum', 'pic']
        self.wirter = csv.DictWriter(csv_f, fieldnames)
        self.wirter.writeheader()  # 写头部

    def send_request(self, url, params=None):
        # print(url)
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            return response

    def parse_content(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        li_list = soup.select('.article li')
        objids = ''
        dict_info = {}
        for li in li_list:
            if len(li.select('a')) != 0:
                title = li.select('h3')[0].get_text()
                href = li.select('a')[0].attrs['href']
                'https://www.autohome.com.cn/news/201911/951360.html#pvareaid=102624'
                print(href)
                result = re.search(r'\d/(.*?).html', href)
                #12312  #2312780-4
                objid = result.group(1).split('-')[0]
                content = li.select('p')[0].get_text()
                time = li.select('.fn-left')[0].get_text()
                vnum = li.select('.fn-right em')[0].get_text()
                pic = li.select('img')[0].attrs['src']
                # objid = li.attrs['data-artidanchor']

                cnum = self.get_comment(objid)
                dict_info['title'] = title
                dict_info['content'] = content
                dict_info['time'] = time
                dict_info['vnum'] = vnum
                dict_info['cnum'] = cnum
                dict_info['pic'] = pic
                self.write_content(dict_info)

    def get_comment(self, objid):
        data = {
            'appid': 1,
            'dateType': 'jsonp',
            'objids': objid
        }
        response = self.send_request(self.c_url, data)
        if response:
            result = response.text.replace("'commentlist'", '''"commentlist"''').replace("(", "").replace(")", "")
            dict_comment = json.loads(result)
            return dict_comment['commentlist'][0]['replycount']

    def write_content(self, info):
        self.wirter.writerow(info)

    def start(self):
        for i in range(1, 3):
            full_url = self.url % (str(i))
            print(full_url)
            response = self.send_request(full_url)
            if response:
                self.parse_content(response)


if __name__ == '__main__':
    qcs = QiCheSpider()
    qcs.start()
