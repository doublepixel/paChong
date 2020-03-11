import ssl
import urllib.request
import urllib.parse
from http.cookiejar import CookieJar

ssl._create_default_https_context = ssl._create_unverified_context


class YaoZhiSpider():
    def __init__(self):
        self.login_url = 'https://www.yaozh.com/login'
        self.member_url = 'https://www.yaozh.com/member/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
            'Cookie': 'acw_tc=2f624a0e15733788678142396e509499a759a662dd9d676ad2d0e80cc3e7bf; UtzD_f52b_saltkey=o00YCFP3; UtzD_f52b_lastvisit=1573375455; _ga=GA1.1.2035857917.1573379059; PHPSESSID=tbev5hkvv9db1e8mrnn6bk8je6; _gid=GA1.2.1691947009.1573529629; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1573529640; yaozh_userId=839463; yaozh_uidhas=1; yaozh_mylogin=1573529644; acw_tc=2f624a0e15733788678142396e509499a759a662dd9d676ad2d0e80cc3e7bf; _ga=GA1.1.2035857917.1573379059; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1573378868%2C1573529629; UtzD_f52b_ulastactivity=1573379039%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D727672; UtzD_f52b_creditbase=0D0D0D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; _gid=GA1.1.640631746.1573544983; UtzD_f52b_lastact=1573545676%09uc.php%09; _gat=1',
            'Referer': 'https://www.yaozh.com/login/proxy',
        }
        self.member_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',

        }
        self.cookiejar = CookieJar()
        self.httpcookieprocessor = urllib.request.HTTPCookieProcessor(self.cookiejar)
        self.opener = urllib.request.build_opener(self.httpcookieprocessor)
        self.form_data = urllib.parse.urlencode({
            "username": "模拟登陆小源",
            "pwd": "qwe123456",
            "formhash": "FD964B294E",
            "backurl": "https%3A%2F%2Fwww.yaozh.com%2Fmember%2F",
        }).encode('utf-8')

    def send_request(self):
        request = urllib.request.Request(self.login_url, data=self.form_data, headers=self.headers)
        response = self.opener.open(request)
        if response.status == 200:
            print('获取cookie成功')
            request = urllib.request.Request(self.member_url, headers=self.member_headers)
            response = self.opener.open(request)
            if response.status == 200:
                print('获取会员页成功')
                self.write_content(response)

    def write_content(self, response):
        with open('yaozhi.html', 'w') as f:
            f.write(response.read().decode())


if __name__ == '__main__':
    yzs = YaoZhiSpider()
    yzs.send_request()
