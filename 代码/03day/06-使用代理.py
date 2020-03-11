import urllib.request
import random
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

'''
:16816
'''

proxy_list = [
    {"https": "171.35.160.182:9999"},
    {"https": "183.164.238.70:9999"},
    {"https": "123.54.45.133:9999"},
    {"https": "59.57.148.235:9999"},
]

proxies = random.choice(proxy_list)

# authproxy = {
#     "https": "188.131.173.36:16816"
# }

authproxy = {
    "https": "496155678:tx4p1gbw@188.131.173.36:16816"
}

proxyhandler = urllib.request.ProxyHandler(
    proxies=authproxy
)
# 创建一个opener
opener = urllib.request.build_opener(proxyhandler)

request = urllib.request.Request(url=url, headers=headers)

response = opener.open(request)

print(response.status)
