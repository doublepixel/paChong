# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings
import scrapy

import os

IMAGES_STORE = get_project_settings().get('IMAGES_STORE')


class WangzherongyaoPipeline(object):
    def process_item(self, item, spider):
        return item


class WangZheImagePipeline(ImagesPipeline):
    # # 重写了发送图片请求
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['pic'])

    # 重写
    def item_completed(self, results, item, info):
        print(results)
        paths = [x['path'] for ok, x in results if ok]
        os.rename(IMAGES_STORE + '/' + paths[0],
                  IMAGES_STORE + '/' + 'full/' + item['cname'] + '_' + item['skinname'] + '.jpg')
        return item
