# -*- coding: utf-8 -*-

# Scrapy settings for zhilianzhaopin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhilianzhaopin'

SPIDER_MODULES = ['zhilianzhaopin.spiders']
NEWSPIDER_MODULE = 'zhilianzhaopin.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 一般不遵守

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Cookie': 'x-zp-client-id=f746022e-afb5-4810-a5a3-ea0541c3fb76; adfbid2=0; sts_deviceid=16de95254d65d3-0d0de0b8ba7f69-38647b00-1024000-16de95254d7323; __utmz=269921210.1571577550.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); dywez=95841923.1571577550.1.1.dywecsr=(direct)|dyweccn=(direct)|dywecmd=(none)|dywectr=undefined; sou_experiment=unexperiment; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; acw_tc=3da2311815746641947011608eb5d5fe4578108d84bc4c896b73c025df; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216de952561a1f5-019be99915c5b2-38647b00-1024000-16de952561b2ca%22%2C%22%24device_id%22%3A%2216de952561a1f5-019be99915c5b2-38647b00-1024000-16de952561b2ca%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baiduPC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2C%22%24latest_utm_campaign%22%3A%22pp%22%2C%22%24latest_utm_content%22%3A%22tj%22%2C%22%24latest_utm_term%22%3A%2228943119%22%7D%7D; urlfrom2=121126445; adfcid2=none; dywea=95841923.1412118538982673200.1571577550.1571895572.1574664197.5; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1574510371,1574664198; __utma=269921210.2072672739.1571577550.1571895572.1574664198.5'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhilianzhaopin.middlewares.ZhilianzhaopinSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'zhilianzhaopin.middlewares.ZhilianzhaopinDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhilianzhaopin.pipelines.ZhilianzhaopinPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
