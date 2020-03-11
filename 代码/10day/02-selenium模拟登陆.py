from selenium import webdriver
import urllib.parse
import re
import time
import requests
import pytesseract
from PIL import Image
import http.client, mimetypes, urllib, json


class V2exSpider():
    def __init__(self):
        self.url = 'https://www.v2ex.com/signin'
        self.driver = webdriver.Chrome(
            executable_path='/Users/xiaoyuan/Downloads/chromedriver'
        )
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'referer': 'https://www.v2ex.com/signin',
        }

    def send_request(self):
        self.driver.get(self.url)
        time.sleep(2)
        url = self.code_url()  # 获取验证码地址
        print(url)
        self.get_cookie()  # 获取Cookie
        response = self.send_code_request(url)  # 发起图片请求
        self.save_code(response)

        # 手动
        # code = input('请输入验证码')
        # print(code)

        inputs = self.driver.find_elements_by_xpath('//input[@class="sl"]')[2]
        print(inputs)
        inputs.send_keys('1')

        # jiqi

        # img = Image.open('code.png')
        # result = pytesseract.image_to_string(img)
        # print(result)

        # yundama

        # result = getResult('code.png', 3006, 20)
        # print(result)

        '''
        找到那个输入验证码的输入框 
        '''

    def code_url(self):
        pattern = re.compile(r'<div.*?"background-image:.*?\(\'(.*?)\'\);')
        result = re.search(pattern, self.driver.page_source)
        url = urllib.parse.urljoin(self.url, result.group(1))
        return url
        '''
        https://www.v2ex.com/_captcha?once=94520
        https://www.v2ex.com/_captcha?once=27903
        '''

    def send_code_request(self, url):
        response = requests.get(url, headers=self.headers)
        return response

    def save_code(self, response):
        with open('code.png', 'wb') as f:
            f.write(response.content)

    def get_cookie(self):
        print(self.driver.get_cookies())
        cookie = [item["name"] + "=" + item["value"] for item in self.driver.get_cookies()]
        cookiestr = ';'.join(item for item in cookie)
        self.headers['Cookie'] = cookiestr

    def start(self):
        self.send_request()


class YDMHttp:
    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb');
        res = requests.post(url, files=files, data=fields)
        return res.text


######################################################################

# 用户名
username = 'zhaoqingyuan'

# 密码
password = '123456'

# 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
appid = 6492

# 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
appkey = '70c7a9590394eb1e42c6b0224446ebb8'

# 图片文件
filename = 'getimage.jpg'

# 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
codetype = 1004

# 超时时间，秒
timeout = 60


def getResult(filename, codetype, timeout):
    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login()
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance()
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout);
        return result
        print('cid: %s, result: %s' % (cid, result))


######################################################################


if __name__ == '__main__':
    v2s = V2exSpider()
    v2s.start()
