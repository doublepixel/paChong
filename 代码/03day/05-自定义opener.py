import urllib.request

url = 'http://www.baidu.com/'
# urllib.request.urlopen()
# 创建一个HTTP处理的
httphandler = urllib.request.HTTPHandler()
# httphandler = urllib.request.HTTPSHandler()
# 创建一个opener
opener = urllib.request.build_opener(httphandler)
response = opener.open(url)
print(response.status)
