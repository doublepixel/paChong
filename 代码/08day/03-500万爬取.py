import requests
import re
import pymysql


class WuBaiWanSpider():
    def __init__(self):
        self.url = 'https://kaijiang.500.com/static/info/kaijiang/xml/ssq/list.xml?_A=DMHOCVAE1574058534107'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        }
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='123456',
                                          db='db_1903')
        self.cursor = self.connection.cursor()

    def send_request(self):
        response = requests.get(url=self.url, headers=self.headers)
        if response.status_code == 200:
            return response

    def parse_content(self, response):
        pattern = re.compile(r'opencode="(.*?)".*?opentime="(.*?)"', re.S)
        result = re.findall(pattern, response.text)
        self.write_mysql(result)

    def write_mysql(self, result):
        # [(),()]
        for info in result:
            red_ball = info[0].split("|")[0]
            blue_ball = info[0].split("|")[1]
            time_info = info[1]
            sql = ''' insert into `tbl_seq` (`red`,`blue`,`time`) values (%s,%s,%s)
            '''
            print(red_ball, blue_ball)
            self.cursor.execute(sql, [red_ball, blue_ball, time_info])
            self.connection.commit()

    def start(self):
        reponse = self.send_request()
        if reponse:
            self.parse_content(reponse)


if __name__ == '__main__':
    wbws = WuBaiWanSpider()
    wbws.start()
