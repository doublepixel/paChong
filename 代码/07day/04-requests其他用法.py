import requests
from lxml import etree
from bs4 import BeautifulSoup

# url = 'https://httpbin.org/post'
# files = {'file': open('image.jpg', 'rb')}
# response = requests.post(url, files=files)
# print(response.text)

# 代理
# proxy = {
#     'HTTPS': '120.83.100.51:9999',
#     'HTTP': '117.69.200.187:9999'
# }
# # 私密代理
# # proxy = {
# #     "http": "name:password@11.134.156.126:4532"
# # }
# url = 'https://www.baidu.com/'
# response = requests.get(url, proxies=proxy)
# print(response.status_code)
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'Referer': 'https://fly.layui.com/user/login/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Cookie': 'UM_distinctid=16e363d264611a-0132fe9f034f24-12386a5a-fa000-16e363d2647df; __gads=Test; fly-layui=s%3Aqv9lvkDidofZ_oiABSRTPjUPEl6BcmWx.Ipjn0UvRl8p0gpUxyLvUe43kftoFTfgDzWPFg%2B0a7Fs; Hm_lvt_d214947968792b839fd669a4decaaffc=1573393761,1573396095,1573655277,1573796794; Hm_lpvt_d214947968792b839fd669a4decaaffc=1573799518',
    'Host': 'fly.layui.com',
    'ETag': 'W/"2ebf-PFctuXOx3qdbqO1XTknMFszW9IY"'
}
sess = requests.session()
url = 'https://fly.layui.com/user/login/'

response = sess.get(url=url, headers=headers)
html = etree.HTML(response.text)
soup = BeautifulSoup(response.text, 'lxml')
code_url = soup.select('.fly-imagecode')[0]['src']

secret = html.xpath('//input[@name="secret"]/@value')[0]
print(secret)
print("https://fly.layui.com" + code_url)
img_res = sess.get('https://fly.layui.com' + code_url)
print(response.status_code)
with open('code.html', 'wb') as f:
    f.write(img_res.content)

code = input('请输入验证码')
form_data = {
    'secret': secret,
    'loginName': '17600572971',
    'pass': '123456',
    'imagecode': code,

}
print(form_data)
response = sess.post(url=url, data=form_data, headers=headers)
print(response.json())
colection_url = 'https://fly.layui.com/user/post/#collection'
response = sess.get(url=colection_url, headers=headers)
print(response.text)
