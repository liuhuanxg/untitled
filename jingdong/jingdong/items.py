# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:

    phone_name = scrapy.Field()     #商品名称
    price = scrapy.Field()          #商品价格
    commit = scrapy.Field()         #评价数目
    shop_name = scrapy.Field()      #商铺名称
    icons = scrapy.Field()          #经营方式
    crawl_time = scrapy.Field()          #经营方式
