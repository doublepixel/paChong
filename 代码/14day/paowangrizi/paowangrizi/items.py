# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PaowangriziItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    vnum = scrapy.Field()
    cnum = scrapy.Field()
    author = scrapy.Field()
    time = scrapy.Field()
    content = scrapy.Field()
