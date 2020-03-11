### 一、通用爬虫

CrawlSpider它是Spider的派生类，Spider类的设计原则是只爬取start_url列表中的网页，而CrawlSpider类定义了一些规则Rule来提供跟进链接的方便的机制，从爬取的网页结果中获取链接并继续爬取的工作．

### 二、代码参考

```python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#通用爬虫提取到的连接会构建一个Link对象
from scrapy.link import Link
from xiachufang.items import XiachufangItem
#创建通用爬虫的命令：scrapy genspider -t crawl 爬虫名称　域
class XcfcrawlspiderSpider(CrawlSpider):
    #爬虫名称
    name = 'xcfCrawlSpider'
    #设置允许爬取的域
    allowed_domains = ['xiachufang.com']
    #设置起始的url
    start_urls = ['http://www.xiachufang.com/category/']
    # rules:是一个元组（列表）,里面存放的是规则Rule规则对象
    # 可以有多个规则
    #Rule:
    #LinkExtractor:设置提取规则
    #callback:设置回调函数（获取响应,解析数据）
    #follow:设置是否需要跟进
    rules = (
        #分类列表地址
        # http://www.xiachufang.com/category/40073/
        Rule(
            LinkExtractor(allow=r'.*?/category/\d+/'),
            callback='parse_item',
            follow=True,
            process_links='check_category_url'
        ),
        # 菜单详情地址,
        # http://www.xiachufang.com/recipe/1055105/
        # http://www.xiachufang.com/recipe/12137/
        # http://www.xiachufang.com/recipe/100147684/
        Rule(
            LinkExtractor(
                allow=r'.*?/recipe/\d+/',
            ),
            callback='parse_caipu_detail',
            follow=False,
        )
    )
    # def parse(self): 一定不能出现这个方法,因为crawlSpider使用了这个方法
    def parse_item(self, response):
        print('分类获取成功')
        print(response.status,response.url)
    def check_category_url(self,links):
        """
        可以在此方法做对规则提取的url构建成的的link对象做过滤处理
        :param links:
        :return:
        """
        print('===================',links,'===================')
        return links
    def parse_caipu_detail(self,response):
        """
        菜谱详情请求成功后的结果处理,从响应结果中提取目标数据
        :param response:
        :return:
        """
        print('详情获取成功')
        print(response.status,response.url)
        # 取出item
        item = XiachufangItem()
        # 图片链接
        item['coverImage'] = response.xpath('//div[@class="cover image expandable block-negative-margin"]/img/@src').extract_first('')
        # 名称
        item['title'] = ''.join(response.xpath('//h1[@class="page-title"]/text()').extract()).replace(' ','').replace('\n','')
        # 评分
        item['score'] = response.xpath('//div[@class="score float-left"]/span[@class="number"]/text()').extract_first('')
        # 多少人做过
        item['doitnum'] = response.xpath('//div[@class="cooked float-left"]/span[@class="number"]/text()').extract_first('')
        # 发布人
        item['author'] = response.xpath('//div[@class="author"]/a[1]/span/text()').extract_first('')
        # 获取用料的列表
        # 对吓：8只;对吓：8只;对吓：8只;对吓：8只;对吓：8只
        tr_list = response.css('div.ings tr')
        used_list = []
        for tr in tr_list:
            name = ''.join(tr.css('td.name ::text').extract()).replace('\n', '').replace(' ', '')
            value = ''.join(tr.css('td.unit ::text').extract()).replace('\n', '').replace(' ', '')
            if len(value) == 0:
                value = '若干'
            used_list.append(name + ':' + value)
        item['used'] = ';'.join(used_list)
        # 获取做法
        item['methodway'] = '->'.join(response.css('div.steps p.text ::text').extract())
        print(item)
        # yield item

```

> **注意千万记住** ：callback 千万不能写 parse



- deny=（）不抓取的规则，一般较少会用到，当条件复杂时，可以和allow配合一起用，前后夹击，参数和allow一样。
- allowdomains=() 这个和spider类里的allowdomains是一个作用，抓取哪个域名下的网站，前面写了，这个就不用管了。
- denydomains=（）和allowdomains相反，拒绝哪个域名下的网站。
- restirct_xpaths=()，estricc_css()在网页哪个区域里提取链接，可以用xpath表达式和css表达式这个功能是划定提取链接的位置，让提取更加精准。
- tags=('a', 'area')默认提取a标签和area标签
- attrs=('href',)默认提取tags里的href属性，也就是url链接。
- canonicalize=True 文档里说的是url规范化，在scrapy的util文件夹里的url文件，我翻了一遍没找到，文档里说默认数值是true，我的源码是false，我改成了true，没发现有什么变化。
- unique就是说这个地址是不是要规定唯一的，默认true，重复收集一样的地址也没意义不是。
- strip这个是把地址前后多余的空格删除，很有必要。
- process_value=None这个作用比较强大了，他接受一个函数，可以立即对提取到的地址做加工，比如提取用js写的链接，官方文档给了一个例子。
- deny_extensions，排除非网页链接，默认是None，scrapy会给你排除掉以下链接

