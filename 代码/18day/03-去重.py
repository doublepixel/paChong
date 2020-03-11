import redis
from pybloom import BloomFilter

bl = BloomFilter(capacity=10000, error_rate=0.001)
url = 'http://www.wanfangdata.com.cn/details/detaype=conference&id=7363410'
bl.add(url)

print(url in bl)
url1 = 'http://www.wanfangdata.com.cn/details/detaype=conference&id=73634101'
print(url1 in bl)
