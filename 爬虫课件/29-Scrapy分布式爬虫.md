### 一、分布式爬虫

![](http://tp.jikedaohang.com/20191118222927_5BdHwo_5c178bee8f486.jpeg)

### 二、配置

- 去重

- ```
  DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
  ```

- 调度器

- ```
  SCHEDULER = "scrapy_redis.scheduler.Scheduler"
  ```

- 允许暂停

- ```
  SCHEDULER_PERSIST = True
  ```

  

- 队列模式

- ```
  #SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"# 优先级顺序
  #SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"#先进先出
  #SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"#先进后出
  
  ```

  

- 管道文件

- ```
  ITEM_PIPELINES = {
      'example.pipelines.ExamplePipeline': 300,
      'scrapy_redis.pipelines.RedisPipeline': 400,
  }
  ```

  

- Redis配置

- ```
  REDIS_HOST = 'redis的主机的ip'
  REDIS_PORT = '6379'
  ```

  