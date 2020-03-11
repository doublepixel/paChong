import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.douban.com/people/188594987/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'Cookie': 'bid=6S_0q-qy37g; __yadk_uid=TLIw3ogRKPzuJOaUYCoEFYeoskFzMuUN; trc_cookie_storage=taboola%2520global%253Auser-id%3Da36cf50f-9859-40cd-bef2-c46731134903-tuct44fceb4; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18859; ll="108288"; __utmz=30149280.1573440942.8.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1573527347%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3Df3Xb2MPFXtK7JILmgSGNsQaj1Q2iwSdv0D2ZrtzMZ36nyLxR4kti2diZpZMbQawu%26wd%3D%26eqid%3Dad02025a0008d90f000000035dc8cda1%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1645085133.1568646286.1573440942.1573527350.9; __utmc=30149280; ap_v=0,6.0; __utmt=1; dbcl2="188594987:q7grxnGcZyk"; ck=14cQ; _pk_id.100001.8cb4=c995cce0f24e3d23.1568646272.9.1573528607.1573440933.; __utmb=30149280.18.10.1573527350'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

with open('douban.html', 'wb') as f:
    f.write(response.read())
