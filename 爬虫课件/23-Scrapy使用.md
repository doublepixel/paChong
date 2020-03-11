### 一、创建项目

```python
scrapy startproject myspider
```

### 二、目录介绍

- ![](http://tp.jikedaohang.com/20191117220023_MotbZQ_Screenshot.jpeg)

### 三、创建爬虫项目

```python
scrapy genspider jobbole jobbole.com
```

### 四、分析Item字段



### 五、爬虫逻辑

> name = "" ：爬虫唯一名字。

> allow_domains = [] 允许爬虫爬取的域。

> start_urls = () ：爬虫的起始URLS。

> parse(self, response) ：解析数据的地方
>
> 解析数据。
>
> 提取下一页URL。

