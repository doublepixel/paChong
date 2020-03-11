### 常用设置

- 代理

  ```
  USER_AGENT = ''
  ```

- ROBOT协议

- ```
  ROBOTSTXT_OBEY = True
  ```

- 最大并发量 

  并发是指同时处理的request的数量。其有全局限制和局部(每个网站)的限制。Scrapy默认的全局并发限制对同时爬取大量网站的情况并不适用，因此您需要增加这个值。 增加多少取决于您的爬虫能占用多少CPU。 一般开始可以设置为 100 。不过最好的方式是做一些测试，获得Scrapy进程占取CPU与并发数的关系。 为了优化性能，您应该选择一个能使CPU占用率在80%-90%的并发数

- ```
  CONCURRENT_REQUESTS = 32  # 默认32
  ```

- 下载延迟

  单位秒，支持小数，一般都是随机范围：0.5DOWNLOAD_DELAY 到 1.5DOWNLOAD_DELAY 之间

- ```
  DOWNLOAD_DELAY = 3
  ```

- 下载超时

  如果您对一个非常慢的连接进行爬取(一般对通用爬虫来说并不重要)， 减小下载超时能让卡住的连接能被快速的放弃并解放处理其他站点的能力。

- ```
  DOWNLOAD_TIMEOUT = 15
  ```

  

- 是否携带Cookie

  除非您 真的 需要，否则请禁止cookies。在进行通用爬取时cookies并不需要， (搜索引擎则忽略cookies)。禁止cookies能减少CPU使用率及Scrapy爬虫在内存中记录的踪迹，提高性能。

- ```
  COOKIES_ENABLED = False
  ```

- 日志

  当进行通用爬取时，一般您所注意的仅仅是爬取的速率以及遇到的错误。 Scrapy使用 INFO log级别来报告这些信息。为了减少CPU使用率(及记录log存储的要求), 在生产环境中进行通用爬取时您不应该使用 DEBUG log级别。 不过在开发的时候使用 DEBUG 应该还能接受。

- ```
  LOG_FILE = "TencentSpider.log"
  LOG_LEVEL = "INFO"
  LOG_ENCODING = ''
  # 级别
  CRITICAL - 严重错误
  ERROR - 一般错误
  WARNING - 警告信息
  INFO - 一般信息
  DEBUG - 调试信息
  
  ```

- 禁止重试

  对失败的HTTP请求进行重试会减慢爬取的效率，尤其是当站点响应很慢(甚至失败)时， 访问这样的站点会造成超时并重试多次。这是不必要的，同时也占用了爬虫爬取其他站点的能力。

- ```
  RETRY_ENABLED = False
  ```

- 配置请求头

  ```
  DEFAULT_REQUEST_HEADERS={{
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en',
      'User-Agent':'......'   #在这里配置你的请求头
  }}
  ```