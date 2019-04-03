# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import  RedisSpider

class S1Spider(RedisSpider):
    name = 's1'
    # allowed_domains = ['shengshi.com']
    redis_key = ''
    start_urls = []
    url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/index.html'
    start_urls.append(url)
    def parse(self, response):
        city1_list=response.xpath('//tr[@class="provincetr"]/td/a')
        for city1s in city1_list:
            city1=city1s.xpath('./text()').extract_first()
            city2_href=city1s.xpath('./@href').extract_first()
            if city2_href is not  None:
                new_href=response.urljoin(city2_href)
                yield scrapy.Request(url=new_href,meta={'city1':city1},callback=self.city2)

    def city2(self, response):
        pass