import urllib.request
import urllib.parse
import ssl

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'

formdata = {
    'i': '男人',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION',
    'typoResult': 'false',
}
# 取消验证
context = ssl._create_unverified_context()

# 编码并转成Unicode
formdata = urllib.parse.urlencode(formdata).encode('utf8')

# 创建request
request = urllib.request.Request(url=url, data=formdata, headers=headers)

# 发送请求
response = urllib.request.urlopen(request, context=context)

print(response.read())
