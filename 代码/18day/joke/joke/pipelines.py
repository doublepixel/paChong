# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json


class JokePipeline(object):

    def __init__(self):
        self.f = open('joke.txt', 'a')

    def process_item(self, item, spider):
        self.f.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
        return item
