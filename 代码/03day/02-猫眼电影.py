import urllib.request
import ssl
import re
import pymysql
import time
import csv

ssl._create_default_https_context = ssl._create_unverified_context


class MaoYanSpider():
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        }

        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='123456',
                                          db='db_1903')

        self.cursor = self.connection.cursor()

        # 写入csv
        csv_f = open('movies.csv', 'a',encoding='utf-8-sig')
        fieldnames = ['rank', 'pic', 'name', 'actor', 'time', 'grade']
        self.wirter = csv.DictWriter(csv_f, fieldnames)
        self.wirter.writeheader()  # 写头部

    def send_request(self, url):
        request = urllib.request.Request(url=url, headers=self.headers)

        response = urllib.request.urlopen(request)
        if response.status == 200:
            return response

    def parse(self, response):
        content = response.read().decode()
        pattern = re.compile(
            r'<dd>.*?>(.*?)<.*?data-src="(.*?)".*?<p.*?class="name">.*?>(.*?)<.*?<p.*?class="star">(.*?)<.*?<p.*?class="releasetime">(.*?)<.*?<i.*?>(.*?)</i>.*?<i.*?>(.*?)<.*?</dd>',
            re.S)

        result = re.findall(pattern, content)

        for movie in result:
            dict_movie = {}
            dict_movie['rank'] = movie[0]
            dict_movie['pic'] = movie[1]
            dict_movie['name'] = movie[2]
            dict_movie['actor'] = movie[3]
            dict_movie['time'] = movie[4]
            dict_movie['grade'] = movie[5] + movie[6]
            self.write_mysql(dict_movie)
            self.write_csv(dict_movie)

    def write_csv(self, dict_movie):
        self.wirter.writerow(dict_movie, )

    def write_mysql(self, content):
        sql = 'insert into `tbl_movies` (%s) values (%s)' % (
            ','.join([k for k in content.keys()]), ','.join(["%s"] * len(content))
        )
        print(sql)
        self.cursor.execute(sql, [v for v in content.values()])
        self.connection.commit()

    def start(self):
        for i in range(1, 11):
            offset = (i - 1) * 10
            full_url = self.url + str(offset)
            print(full_url)
            response = self.send_request(full_url)
            # print(response.read().decode())
            self.parse(response)
            time.sleep(1)


if __name__ == '__main__':
    mys = MaoYanSpider()
    mys.start()
