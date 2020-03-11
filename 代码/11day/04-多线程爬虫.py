from threading import Thread
from queue import Queue

import requests
import threading
import time
import re


# 爬虫--->生产者
class CrawlSpider(Thread):
    def __init__(self, name, params_queue, data_queue):
        super().__init__()
        self.url = 'https://search.jiayuan.com//v2/search_v2.php'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
        }
        self.name = name
        self.params_queue = params_queue
        self.data_queue = data_queue

    def run(self):
        while True:
            if not self.params_queue.empty():
                params = self.params_queue.get()
                if isinstance(params, dict):
                    response = requests.post(self.url, headers=self.headers, data=params)
                    self.data_queue.put(response.text)
                else:
                    data = params.replace("\\", "")
                    response = requests.get(data, headers=self.headers)
                    self.data_queue.put(response.content)
                time.sleep(1)
            else:
                print(self.name)
                self.data_queue.put('stop')
                break


# 解析爬虫---->消费者
class ParseSpider(Thread):
    def __init__(self, name, data_queue, params_queue):
        super().__init__()
        self.name = name
        self.data_queue = data_queue
        self.params_queue = params_queue

    def run(self):
        while True:
            if not self.data_queue.empty():
                data = self.data_queue.get()
                if isinstance(data, str):
                    pattern = re.compile(r'"image":.*?"(.*?)",', re.S)
                    data = re.findall(pattern, data)
                    for url in data:
                        self.params_queue.put(url)
                else:
                    print('正在保存')
                    ts = str(time.time() * 1000)
                    with open("jiayuan/" + ts + '.jpg', 'wb') as f:
                        f.write(data)
                if data == 'stop':
                    print(self.name)
                    break
                time.sleep(0.5)


class JiaYuanSpider():

    def __init__(self):
        self.params_queue = Queue()  # 参数
        self.data_queue = Queue()  # 返回的数据

    def start(self):

        for i in range(1, 5):
            data = {
                "sex": " f",
                "key": "开朗",
                "stc": "1:11,2:22.30,3:155.170,23:1",
                "sn": "default",
                "sv": "1",
                "p": str(i),
                "f": " search",
                "listStyle": " bigPhoto",
                "pri_uid": " 229235102",
                "jsversion": " v5",
            }
            self.params_queue.put(data)

        crawl_names = ['爬虫1号', '爬虫2号', "'爬虫3号'"]
        for name in crawl_names:
            cs = CrawlSpider(name, self.params_queue, self.data_queue)
            cs.start()

        parse_names = ['解析1号', '解析2号', "'解析3号'"]
        for name in parse_names:
            cs = ParseSpider(name, self.data_queue, self.params_queue)
            cs.start()



if __name__ == '__main__':
    jys = JiaYuanSpider()
    jys.start()
