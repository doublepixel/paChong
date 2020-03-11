import urllib.parse

url = 'https://book.qidian.com/info/1004608738#Catalog'
result = urllib.parse.urlparse(url, allow_fragments=True)
# print(result.fragment)
print(result)

u = ('https', 'book.qidian.com', '/info/1004608738', '', '', 'Catalog')
result = urllib.parse.urlunparse(u)
print(result)

base_url = 'https://book.qidian.com/info/1004608738?wd=123&page=20#Catalog'
sub_url = '/info/100861102'
result = base_url.split('/info')[0] + sub_url
print(result)
# result = urllib.parse.urljoin(base_url,sub_url)
# print(result)


parmas_str = 'page=20&wd=123&wd=456'
result = urllib.parse.parse_qs(parmas_str)
print(result)



wd = '中国梦'
result = urllib.parse.quote(wd)
print(result)

kw = {'wd': "中国梦"}
result = urllib.parse.urlencode(kw)
print(result)


wd = '%E4%B8%AD%E5%9B%BD%E6%A2%A6'
result = urllib.parse.unquote(wd)
print(result)

wd = 'wd=%E4%B8%AD%E5%9B%BD%E6%A2%A6'
result = urllib.parse.unquote(wd)
print(result)