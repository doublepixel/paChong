import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
}
response = requests.get('https://www.baidu.com/', headers=headers)

print(response.text)  # 解码 大部分都能解出来
print(response.content)  # 二进制
print(response.content.decode('utf8'))  # 二进制
print(response.headers)  # 响应头
print(response.url)  # 发起url
print(response.cookies)  # cookie
print(response.status_code)  # 响应码
print(response.encoding)  # 获取当前网站编码类型
print(response.status_code)  # 响应码
with open('baidu.html', 'wb') as f:
    f.write(response.content)
