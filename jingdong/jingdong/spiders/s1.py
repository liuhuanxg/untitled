# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from  ..items import JingdongItem
import datetime

class S1Spider(scrapy.Spider):
    name = 's1'
    allowed_domains = ['jiongdong.com']
    start_urls = []

    base_url='https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=shouji&enc=utf-8'
    start_urls.append(base_url)
    def parse(self, response):
        content=response.body.decode('utf-8')
        # with open('jg.html','w',encoding='utf-8') as fp:
        #     fp.write(content)
        tree=etree.HTML(content)
        Div=tree.xpath('//div[@class="gl-i-wrap"]')
        print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&',len(Div))
        for div_list in Div:
            try:
                phone_name = div_list.xpath('./div[@class="p-name p-name-type-2"]/a/em/text()')
                price=div_list.xpath('./div[@class="p-price"]/strong/i/text()')
                commit = div_list.xpath('./div[@class="p-commit"]/strong/a/text()')
                shop_name=div_list.xpath('./div[@class="p-shop"]/span/a/text()')
                icons=div_list.xpath('./div[@class="p-icons"]/i/text()')
                print(price,phone_name,commit,shop_name,icons)

                jd=JingdongItem()
                jd['phone_name']=phone_name
                jd['price']=price
                jd['commit']=commit
                jd['shop_name']=shop_name
                jd['icons']=icons
                jd['crawl_time']=datetime.datetime.now()
                yield jd
            except:
                pass

