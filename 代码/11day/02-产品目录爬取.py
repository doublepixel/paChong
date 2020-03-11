import requests
import execjs

#
# url = 'http://www.300600900.cn/'
# headers = {
#
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
# }
# response = requests.get(url=url, headers=headers)
# with open('chanpin.html', 'w') as f:
#     f.write(response.text)

'''
1、算出往cookie里面塞的值
2、方法算出这个地址去访问
3、再去访问http://www.300600900.cn/
'''

# 获取执行js的对象
ej = execjs.get()
js_name = 'product.js'
node = ej.compile(open(js_name).read())

cookie_data = node.eval('cookie_data')
security_verify_data = node.eval('security_verify_data')

url = 'http://www.300600900.cn'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
}
key, value = cookie_data.split("=")
session = requests.session()

session.get(url=url, headers=headers)
# 把算出的cookie加入到这里面
session.cookies.set(key, value)

# 要去访问的地址
full_url = url + security_verify_data
session.get(full_url, headers=headers)

# 再去访问主页

response = session.get(url, headers=headers)

with open('chanpin1.html', 'w') as f:
    f.write(response.content.decode())
