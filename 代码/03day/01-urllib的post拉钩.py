import urllib.request
import urllib.parse
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context


class LaGouSpider():
    def __init__(self):
        self.url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
            'Cookie': '_ga=GA1.2.288895507.1571063606; user_trace_token=20191014223325-94eae50c-ee8f-11e9-a5a9-5254005c3644; LGUID=20191014223325-94eae829-ee8f-11e9-a5a9-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216dcab0494d2-096396c7aa258b-38647b00-1024000-16dcab0494e835%22%2C%22%24device_id%22%3A%2216dcab0494d2-096396c7aa258b-38647b00-1024000-16dcab0494e835%22%7D; JSESSIONID=ABAAABAAAFCAAEG1B13739A74C6FAAB472D371EE749F45A; WEBTJ-ID=20191111091527-16e5807aa5fcc-030596f070f49f-1d3f6a5a-786432-16e5807aa614e9; _gid=GA1.2.975002822.1573434928; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1571063606,1572832750,1573195279,1573434928; LGSID=20191111091528-bf8f4ad4-0420-11ea-a485-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; X_MIDDLE_TOKEN=71cd53a12ab8208ea9f441a1d674b588; LGRID=20191111091613-da5e8916-0420-11ea-a62c-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1573434974; SEARCH_ID=1c842748442947d28410b4cf58c3acae; X_HTTP_TOKEN=d21ae80690939c74389434375186e918d2d7d2d9fc'
        }
        self.result = []  # 保存数据

    def send_request(self, form_data):
        # 创建请求
        request = urllib.request.Request(url=self.url, data=form_data, headers=self.headers)
        # 发送请求
        response = urllib.request.urlopen(request)
        if response.status == 200:
            return response

    def parse(self, response):
        content = response.read().decode()  # 字符串

        dict_result = json.loads(content)

        if not self.result:
            self.result = dict_result
        else:
            self.result['content']['positionResult']['result'] = self.result.get('content').get(
                'positionResult').get('result') + dict_result.get('content').get('positionResult').get('result')

    def write_json(self, content):
        with open('position.json', 'a') as f:
            f.write(content + "\n")

    def start(self):
        for i in range(1, 3):
            form_data = {
                'first': 'true',
                'pn': str(i),
                'kd': 'python',
            }
            form_data = urllib.parse.urlencode(form_data).encode('utf8')
            reponse = self.send_request(form_data)
            if reponse:
                self.parse(reponse)
        self.write_json(json.dumps(self.result))


if __name__ == '__main__':
    lgs = LaGouSpider()
    lgs.start()
