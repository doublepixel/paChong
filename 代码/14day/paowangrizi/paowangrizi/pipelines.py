# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class PaowangriziPipeline(object):

    def __init__(self, host, user, password, db):
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          db=db)

        self.cursor = self.connection.cursor()

    @classmethod
    def from_crawler(cls, crawler):
        host = crawler.settings['MYSQL_HOST']
        port = crawler.settings['MYSQL_PORT']
        user = crawler.settings['MYSQL_USER']
        pwd = crawler.settings['MYSQL_PWD']
        db = crawler.settings['MYSQL_DB']

        return cls(host, user, pwd, db, port)

    def process_item(self, item, spider):
        '''
        插入数据
        :param item:
        :param spider:
        :return:
        '''

        return item
