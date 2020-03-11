import requests
from lxml import etree
import urllib.parse
import re
from bs4 import BeautifulSoup
from pyecharts.charts import Bar, Page
from pyecharts import options as opts


class WeiBoSpider():
    def __init__(self):
        self.url = 'https://s.weibo.com/weibo?q=%E5%8F%8C%E5%8D%81%E4%B8%80&wvr=6&b=1&Refer=SWeibo_box&page='
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Cookie': 'SINAGLOBAL=1757626456674.1885.1456822965332; _ga=GA1.2.1545216043.1496394652; __gads=ID=5183fdace152c3af:T=1558335578:S=ALNI_MbdL_xmfhvDQsWBo8ULisc_L69YIQ; wvr=6; Ugrow-G0=7e0e6b57abe2c2f76f677abd9a9ed65d; SSOLoginState=1574043175; TC-V5-G0=4de7df00d4dc12eb0897c97413797808; _s_tentry=login.sina.com.cn; UOR=blog.csdn.net,widget.weibo.com,login.sina.com.cn; Apache=1366484569155.0576.1574043179821; wb_view_log_7167901478=1024*7681; ULV=1574043179855:67:4:1:1366484569155.0576.1574043179821:1573789518829; WBtopGlobal_register_version=307744aa77dd5677; SCF=AvyT3ck8JC6OQqaPZ1YQm3oIrmvywqo6vuLyDYE7oG1-ZnUvS2bHgOiKr0_YEOu7VUVVFLaF0NO9tpLHCcAsHPo.; SUB=_2A25w1nRGDeRhGeFP7VUY8C_IzDSIHXVTouKOrDV8PUNbmtAKLUffkW9NQQQwgiL__uoxH4wx-vFOKhOSF4iRfUST; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5rcd0Gxp45iyfa-62726B45JpX5K2hUgL.FoMpSoM4eh2XS0n2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoM4eKnRSonXSo-N; SUHB=0z1A7ILM3N2Iv3; ALF=1574649493; un=17600572971; TC-Page-G0=8afba920d7357d92ddd447eac7e1ec5c|1574044710|1574044661; webim_unReadCount=%7B%22time%22%3A1574044711321%2C%22dm_pub_total%22%3A1%2C%22chat_group_client%22%3A0%2C%22allcountNum%22%3A33%2C%22msgbox%22%3A0%7D'
        }

        self.data = {'100000': 0, '50000': 0, "10000": 0, "5000": 0, '2000': 0, "1000": 0, "10": 0}

    def send_request(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        with open('weibo.html', 'w') as f:
            f.write(response.text)
        if response.status_code == 200:
            return response

    def parse_scontent(self, response):
        html = etree.HTML(response.text)
        div_list = html.xpath('//div[@class="m-con-l"]//div[@class="card-wrap"]')
        for div in div_list:
            href = div.xpath('.//div[@class="avator"]/a/@href')[0]
            name = div.xpath('.//a[@class="name"]/@nick-name')[0]
            href = urllib.parse.urljoin(self.url, href)
            response = self.send_request(href)
            if response:
                self.parse_info(response)

    def parse_info(self, response):
        pattern = re.compile(r'var url = "(.*?)";', re.S)
        result = re.search(pattern, response.text)
        real_url = result.group(1)
        response = self.send_request(real_url)
        if response:
            self.parse_nums(response)

    def parse_nums(self, response):
        with open('weibo2.html', 'w') as f:
            f.write(response.text)
        pattern1 = re.compile(
            r'<strong class=."W_f\d+.">(\d+)<./strong>', re.S)
        result = re.findall(pattern1, response.text)
        print(result)
        if int(result[1]) > 100000:
            self.data['100000'] = self.data['100000'] + 1
        elif int(result[1])  > 50000:
            self.data['50000'] = self.data['50000'] + 1
        elif int(result[1])  > 10000:
            self.data['10000'] = self.data['10000'] + 1
        elif int(result[1])  > 5000:
            self.data['5000'] = self.data['5000'] + 1
        elif int(result[1])  > 2000:
            self.data['2000'] = self.data['2000'] + 1
        elif int(result[1])  > 1000:
            self.data['1000'] = self.data['1000'] + 1
        else:
            self.data['10'] = self.data['10'] + 1

    def write_content(self):
        pass

    def start(self):
        for i in range(1, 16):
            full_url = self.url + str(i)
            response = self.send_request(full_url)
            if response:
                self.parse_scontent(response)
        self.create_bar()  # 绘制表格

    def create_bar(self):
        c = Bar().add_xaxis(list(self.data.keys())).add_yaxis("粉丝数", list(self.data.values())).set_global_opts(
            title_opts=opts.TitleOpts(title="粉丝数分析", subtitle="哈哈哈"))
        Page().add(c).render()


if __name__ == '__main__':
    wbs = WeiBoSpider()
    wbs.start()
