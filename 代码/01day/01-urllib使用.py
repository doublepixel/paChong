import urllib.request

url = 'http://www.baidu.com/'

response = urllib.request.urlopen(url)
print(response.status)  # 获取状态码
print(response.info())  # 获取响应头
print(response.getcode())  # 获取响应头
print(response.geturl())  # 获取状态码

# print(response.read().decode('utf8'))

with open('baidu.html', 'wb') as f:
    f.write(response.read())
