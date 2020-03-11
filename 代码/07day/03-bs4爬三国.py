import requests
import urllib.parse
from bs4 import BeautifulSoup


class SanGuoSpider():
    def __init__(self):
        self.url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
        }

    def send_request(self, url):
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            return response

    def prase_content(self, reponse):
        html = reponse.text
        soup = BeautifulSoup(html, 'lxml')
        a_list = soup.select('.book-mulu>ul>li>a')
        for a in a_list:
            name = a.string
            # print(a.get_text())
            # print(a.text)
            href = a['href']
            detial_url = urllib.parse.urljoin(self.url, href)
            print(detial_url)
            response = self.send_request(detial_url)
            if response:
                self.parse_detail(response, name)

    def parse_detail(self, reponse, name):
        html = reponse.text
        soup = BeautifulSoup(html, 'lxml')
        content = soup.find('div', class_="chapter_content").get_text()
        print(content)
        self.write_content(content, name)

    def write_content(self, content, name):
        with open("sanguo/" + name + ".txt", 'w') as f:
            f.write(content)

    def start(self):
        reponse = self.send_request(self.url)
        if reponse:
            self.prase_content(reponse)


if __name__ == '__main__':
    sgs = SanGuoSpider()
    sgs.start()
