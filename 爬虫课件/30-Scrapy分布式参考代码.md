### 参考代码

- 用Redis去重和分布式

- ```python
  
  from scrapy.linkextractors import LinkExtractor
  from scrapy.spiders import CrawlSpider, Rule
  
  
  class DmozSpider(CrawlSpider):
      """Follow categories and extract links."""
      name = 'dmoz'
      allowed_domains = ['dmoz.org']
      start_urls = ['http://www.dmoz.org/']
  
      rules = [
          Rule(LinkExtractor(
              restrict_css=('.top-cat', '.sub-cat', '.cat-item')
          ), callback='parse_directory', follow=True),
      ]
  
      def parse_directory(self, response):
          for div in response.css('.title-and-desc'):
              yield {
                  'name': div.css('.site-title::text').extract_first(),
                  'description': div.css('.site-descr::text').extract_first().strip(),
                  'link': div.css('a::attr(href)').extract_first(),
              }
  
  
  ```

- 分布式普通爬虫

- ```python
  from scrapy_redis.spiders import RedisSpider
  
  
  class MySpider(RedisSpider):
      """Spider that reads urls from redis queue (myspider:start_urls)."""
      name = 'myspider_redis'
      redis_key = 'myspider:start_urls'
  
      def __init__(self, *args, **kwargs):
          # Dynamically define the allowed domains list.
          domain = kwargs.pop('domain', '')
          self.allowed_domains = filter(None, domain.split(','))
          super(MySpider, self).__init__(*args, **kwargs)
  
      def parse(self, response):
          return {
              'name': response.css('title::text').extract_first(),
              'url': response.url,
          }
  ```

  

- 分布式通用爬虫

- ```python
    
  from scrapy.spiders import Rule
  from scrapy.linkextractors import LinkExtractor
  
  from scrapy_redis.spiders import RedisCrawlSpider
  
  
  class MyCrawler(RedisCrawlSpider):
      """Spider that reads urls from redis queue (myspider:start_urls)."""
      name = 'mycrawler_redis'
      redis_key = 'mycrawler:start_urls'
  
      rules = (
          # follow all links
          Rule(LinkExtractor(), callback='parse_page', follow=True),
      )
  
      def __init__(self, *args, **kwargs):
          # Dynamically define the allowed domains list.
          domain = kwargs.pop('domain', '')
          self.allowed_domains = filter(None, domain.split(','))
          super(MyCrawler, self).__init__(*args, **kwargs)
  
      def parse_page(self, response):
          return {
              'name': response.css('title::text').extract_first(),
              'url': response.url,
          }
  ```

  

### 运行爬虫

```
scrapy runspider myspider_redis.py
lpush myspider:start_urls http://www.dmoz.org/

```

### 处理数据

```python

import json
import redis
import pymysql
def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='localhost', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='localhost', user='用户', passwd='密码', db = '数据库', port=3306, use_unicode=True)
    # 使用cursor()方法获取操作游标
    cur = mysqlcli.cursor()
    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = rediscli.blpop("redis中对应的文件夹:items")
        item = json.loads(data.decode('utf-8'))
        try:
            # 使用execute方法执行SQL INSERT语句
            cur.execute(“插入语句"，['数据'])
            # 提交sql事务
            mysqlcli.commit()
            print("inserted successed")
        except Exception as err:
            #插入失败
            print("Mysql Error",err)
            mysqlcli.rollback()
if __name__ == '__main__':
    main()

```

