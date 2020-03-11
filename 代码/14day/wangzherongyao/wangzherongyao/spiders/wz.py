# -*- coding: utf-8 -*-
import scrapy
import json
from wangzherongyao.items import WangzherongyaoItem


class WzSpider(scrapy.Spider):
    name = 'wz'
    allowed_domains = ['qq.com']
    start_urls = ['https://pvp.qq.com/web201605/js/herolist.json']

    skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'



    def parse(self, response):
        dict_result = json.loads(response.text)
        for res in dict_result:
            cname = res['cname']
            ename = res['ename']
            title = res['title']
            skin_name = res.get('skin_name')
            if skin_name:
                skin_list = skin_name.split("|")
                for index, skin in enumerate(skin_list):
                    full_skin_url = self.skin_url.format(ename, ename, index + 1)
                    item = WangzherongyaoItem()
                    item['cname'] = cname
                    item['ename'] = ename
                    item['title'] = title
                    item['skinname'] = skin
                    item['pic'] = full_skin_url
                    yield item

    'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/113/113-bigskin-1.jpg'
    'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/113/113-bigskin-2.jpg'
    'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/113/113-bigskin-3.jpg'
    'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/113/113-bigskin-4.jpg'
