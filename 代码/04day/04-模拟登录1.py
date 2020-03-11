import urllib.request
from http.cookiejar import CookieJar
import ssl
import urllib.parse

ssl._create_default_https_context = ssl._create_unverified_context

login_url = 'https://wanandroid.com/user/login'

form_data = {
    'username': '496155678@qq.com',
    'password': '123456',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
}

form_data = urllib.parse.urlencode(form_data).encode('utf8')

cookiejar = CookieJar()

# 创建一个处理cookie的handler
httpcookieprocessor = urllib.request.HTTPCookieProcessor(cookiejar)

# 创建一个opener
opener = urllib.request.build_opener(httpcookieprocessor)

# 创建一个request
request = urllib.request.Request(url=login_url, headers=headers)

# 发起请求
response = opener.open(request, data=form_data)

print(response.status)
print(response.read())

collection_url = 'https://wanandroid.com/lg/collect'

response = opener.open(collection_url)

with open('wanandroid.html', 'wb') as f:
    f.write(response.read())
print(response.status)
