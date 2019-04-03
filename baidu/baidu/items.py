# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#存储数据
class JobItem(scrapy.Item):
    # data_info = work_name + ',' + work_type + ',' + num + ',' + place + ',' + time + '\n'
    title=scrapy.Field()
    job_type=scrapy.Field()
    num=scrapy.Field()
    job_local=scrapy.Field()
    realtime=scrapy.Field()