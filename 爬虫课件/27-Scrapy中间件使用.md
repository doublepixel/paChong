### Scrapy中间使用

- UA中间件

  ```python
  USER_AGENTS = [
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
      "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
      "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
      "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
      "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
  ]
  
  # https://fake-useragent.herokuapp.com/browsers/0.1.11
  ```

  ```python
  import random
  class RandomUserAgent(object):
      def process_request(self, request, spider):
          
          #获取到代理的代理池
          useragents = spider.settings['USERAGENTS']
          #随机获取一个User-Agent
          user_agent = random.choice(useragents)
          print('执行下载中间件'+user_agent)
          if user_agent:
              request.headers['User-Agent'] = user_agent
  
  ```

  ```python
  DOWNLOADER_MIDDLEWARES = {
      'mySpider.middlewares.RandomUserAgent': 99,
  }
  
  ```

  

- 代理中间件

  ```python
  PROXIES = [
      {'ip_port': '111.8.60.9:8123', 'type': 'HTTP', 'user_pwd': 'user1:pass1'},
      {'ip_port': '101.71.27.120:80', 'type': 'HTTP', 'user_pwd': 'user2:pass2'},
      {'ip_port': '117.57.91.227:9999', 'type': 'HTTP', 'user_pwd': None},
      {'ip_port': '114.239.251.135:9999', 'type': 'HTTP', 'user_pwd': None},
      {'ip_port': '182.35.87.247:9999', 'type': 'HTTP', 'user_pwd': None},
      {'ip_port': '117.69.201.105:9999', 'type': 'HTTP', 'user_pwd': None},
      {'ip_port': '36.25.42.70:9999', 'type': 'HTTPS', 'user_pwd': None},
      {'ip_port': '114.239.254.13:9999', 'type': 'HTTP', 'user_pwd': None},
      {'ip_port': '59.57.38.252:9999', 'type': 'HTTPS', 'user_pwd': None},
      {'ip_port': '103.10.86.203:8080', 'type': 'HTTP', 'user_pwd': None},
      {'ip_port': '123.139.56.238:9999', 'type': 'HTTPS', 'user_pwd': None},
  ]
  
  ```

  ```
  import random
  import base64
  class ProxyMiddlewares(object):
      def process_request(self, request, spider):
          proxies = spider.settings['PROXIES']
          proxy = random.choice(proxies)
          print(proxy)
          if proxy['user_pwd'] is None:
              # 没有代理账户验证的代理使用方式
              if proxy['type'] == 'HTTP':
                  u = "http://%s" % proxy['ip_port']
                  request.meta['proxy'] = u
              else:
                  u = "https://%s" % proxy['ip_port']
                  request.meta['proxy'] = u
              print(u)
          else:
              # 对账户密码进行base64编码
              user_pwd = base64.b64encode(proxy['user_pwd'].encode('utf-8')).decode('utf-8')
              # 对应到代理服务器的信令格式里
              request.headers['Proxy-Authorization'] = 'Basic ' + user_pwd
              request.meta['proxy'] = "https://%s" % proxy['ip_port']
  
  
  ```

- Cookie中间件

- ```python
  import random
  class RandomCookiesMiddleware(object):
      
      def process_request(self,request,spider):
          cookies = spider.settings['COOKIES']
          #随机获取一个cookies
          cookie = random.choice(cookies)
          if cookie:
              request.cookies = cookie
  
  ```

  

- Selenium中间件

- ```python
  from selenium import webdriver
  from selenium.common.exceptions import TimeoutException
  from scrapy.http import HtmlResponse
  import time
  class SeleniumMiddleware(object):
      def __init__(self):
          self.driver = webdriver.Chrome(executable_path='/Users/xiaoyuan/Downloads/chromedriver')
          self.driver.set_page_load_timeout(10)
  
      def process_request(self, request, spider):
          try:
              url = request.url
              self.driver.get(url)
  
              input = self.driver.find_element_by_id('kw')
              time.sleep(1)
              input.send_keys('美女')
              time.sleep(1)
            btn = self.driver.find_element_by_id('su')
              btn.click()
              time.sleep(3)
              self.driver.save_screenshot('baidu.png')
              btn = self.driver.find_element_by_class_name('n')
              btn.click()
              if self.driver.page_source:
                  return HtmlResponse(url=url, body=self.driver.page_source, status=200, encoding='utf-8',
                                      request=request)
          except TimeoutException:
              print('请求超时')
              return HtmlResponse(url=request.url, body=None, status=500)
  ```
  
  ### process_request(request, spider)
  
  - 如果其返回 `None`： 
    Scrapy将继续处理该request，执行其他的中间件的相应方法，直到合适的下载器处理函数(download handler)被调用， 该request被执行(其response被下载)
  - 如果其返回`Response 对象`： 
    Scrapy将不会调用任何其他的process_request()或 process_exception()方法，或相应的下载函数。其将返回该`response`，已安装的中间件的 process_response() 方法则会在每个response返回时被调用
  - 如果其返回 `Request对象` ： 
    Scrapy则会停止调用 process_request方法并重新调度返回的`request`，也就是把request重新返回，进入调度器重新入队列
  - 如果其返回`raise IgnoreRequest异常` ： 
    则安装的下载中间件的 process_exception()方法 会被调用。如果没有任何一个方法处理该异常， 则request的`errback(Request.errback)`方法会被调用。如果没有代码处理抛出的异常， 则该异常被忽略且不记录(不同于其他异常那样)
  
  ### process_response(request, response, spider)
  
  - 如果其返回一个 `Response对象`： 
    (可以与传入的response相同，也可以是全新的对象)， 该response会被在链中的其他中间件的 process_response() 方法处理
  
  - 如果其返回一个 `Request对象`： 
    则中间件链停止， 返回的request会被重新调度下载。处理类似于 process_request() 返回request所做的那样
  
  - 如果其抛出一个`IgnoreRequest异常` ：
  
    则调用request的`errback(Request.errback)`。 如果没有代码处理抛出的异常，则该异常被忽略且不记录(不同于其他异常那样)
  
  ### process_exception(request, exception, spider)
  
  - 如果其返回 `None` ： 
    Scrapy将会继续处理该异常，接着调用已安装的其他中间件的 process_exception()方法，直到所有中间件都被调用完毕，则调用默认的异常处理
  - 如果其返回一个 `Response 对象`： 
    相当于异常被纠正了，则已安装的中间件链的 process_response()方法被调用。Scrapy将不会调用任何其他中间件的 process_exception()方法
  - 如果其返回一个 `Request 对象`： 
    则返回的request将会被重新调用下载。这将停止中间件的 process_exception() 方法执行，就如返回一个response的那样