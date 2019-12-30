# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoItem(scrapy.Item):
    # define the fields for your item here like:
    title= scrapy.Field()  #商品名称
    price= scrapy.Field()  #现价
    originalPrice= scrapy.Field()  #原价
    sellerLoc= scrapy.Field()  #卖家地址
    sold= scrapy.Field()  #付款人数
    nick= scrapy.Field()  #商家
    crawl_time=scrapy.Field()  #爬取时间
    detail_url=scrapy.Field()  #爬取时间

    sales=scrapy.Field()#销量


