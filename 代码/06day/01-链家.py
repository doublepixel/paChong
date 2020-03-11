import requests
from lxml import etree
import pymysql
import json


class LianJiaSpider():
    def __init__(self):
        self.url = 'https://bj.lianjia.com/chengjiao/pg%d/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }

        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='123456',
                                          db='db_1903')

        self.cursor = self.connection.cursor()

        self.pn = 98

    def send_request(self, url):
        print(url)
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response

    def parse_content(self, response):
        html = etree.HTML(response.text)
        with open('lianjia.html', 'w') as f:
            f.write(response.text)
        li_list = html.xpath('//ul[@class="listContent"]/li')
        for li in li_list:
            pic = li.xpath('./a/img/@src')
            if pic:
                pic = pic[0]
            else:
                pic = ''
            title = li.xpath('.//div[@class="title"]/a/text()')[0]
            houseinfo = "".join(li.xpath('.//div[@class="houseInfo"]/text()'))
            positionInfo = "".join(li.xpath('.//div[@class="positionInfo"]/text()'))
            dealhousetxt = "".join(li.xpath('.//span[@class="dealHouseTxt"]//text()'))
            if not dealhousetxt:
                dealhousetxt = ''
            else:
                dealhousetxt = "".join(dealhousetxt)
            dealcycleeinfo = "".join(li.xpath('.//div[@class="dealCycleeInfo"]//text()'))
            agentinfolist = "".join(li.xpath('.//div[@class="agentInfoList"]/a/text()'))
            dealdate = "".join(li.xpath('.//div[@class="dealDate"]/text()'))
            totalprice = "".join(li.xpath('.//div[@class="totalPrice"]//text()'))
            unitPrice = "".join(li.xpath('.//div[@class="unitPrice"]//text()'))

            dict_home = {}
            dict_home['pic'] = pic
            dict_home['title'] = title
            dict_home['houseinfo'] = houseinfo
            dict_home['positionInfo'] = positionInfo
            dict_home['dealhousetxt'] = dealhousetxt
            dict_home['dealcycleeinfo'] = dealcycleeinfo
            dict_home['agentinfolist'] = agentinfolist
            dict_home['dealdate'] = dealdate
            dict_home['totalprice'] = totalprice
            dict_home['unitPrice'] = unitPrice
            print(dict_home)
            self.write_mysql(dict_home)
        next_text = html.xpath('//div[@class="page-box fr"]//div/@page-data')[0]
        print(next_text)
        totalPage = json.loads(str(next_text))['totalPage']
        if self.pn < totalPage:
            self.pn += 1
            full_url = self.url % (self.pn)
            response = self.send_request(full_url)
            if response:
                self.parse_content(response)

    def write_mysql(self, dict_home):
        sql = "insert into `tbl_lianjia` (`pic`,`title`,`houseinfo`,`positionInfo`,`dealhousetxt`,`dealcycleeinfo`,`agentinfolist`,`dealdate`,`totalprice`,`unitPrice`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql, [v for v in dict_home.values()])
        self.connection.commit()

    def start(self):
        full_url = self.url % (self.pn)
        response = self.send_request(full_url)
        if response:
            self.parse_content(response)


if __name__ == '__main__':
    ljs = LianJiaSpider()
    ljs.start()
