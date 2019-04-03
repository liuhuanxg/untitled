# -*- coding: utf-8 -*-
import scrapy
import jsonpath,json
from ..items import TaobaoItem
import datetime
from urllib import request
from lxml import etree

class S1Spider(scrapy.Spider):
    name = 's1'
    allowed_domains = ['taobao.com']
    start_urls = []

    # base_url='https://s.taobao.com/search?q=%E7%99%BD%E9%85%92&s='
    # base_url='https://s.m.taobao.com/h5?q=%E7%99%BD%E9%85%92&tab=all'
    base_url='https://s.m.taobao.com/search?q=%E7%99%BD%E9%85%92&tab=all&sst=1&n=20&buying=buyitnow&m=api4h5&abtest=10&wlsort=10&page='
    for i in range(1):
        url=base_url+str(i)
        start_urls.append(url)

    def parse(self, response):

        content=response.body.decode('utf-8')
        # with open('taobao.html','w',encoding='utf-8') as fp:
        #     fp.write(content)

        data_dict=json.loads(content)
        listItem=jsonpath.jsonpath(data_dict,'$..listItem.*')

        for product in listItem:
            P=TaobaoItem()
            P['title']=product['title']
            P['price']=product['price']
            P['originalPrice']=product['originalPrice']
            P['sellerLoc']=product['sellerLoc']
            P['sold']=product['sold']
            P['nick']=product['nick']
            P['crawl_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            url=product['url']
            P['detail_url']=url

            #路径拼接
            new_url=request.urljoin(response.url,url)

            #发起详情页请求
            #默认请求地址不允许重复-----为了避免重复请求-----去重
            #dont_filter=True,表示不过滤(url),允许重复请求
            yield scrapy.Request(url=new_url,callback=self.detail_parse,meta={'data':P,'PhantomJS':True},dont_filter=True)
            break
    #解析详情页
    def detail_parse(self,response):
        print('******************************')
        P=response.request.meta['data']
        content=response.body.decode('utf-8')
        tree=etree.HTML(content)
        try:
            sales=tree.xpath('//span[@class="sales"]/text()')
            print(sales)
            P['sales']=sales
        except:
            pass
        # with open('detail.htm','w',encoding='utf-8') as fp:
        #     fp.write(content)
        yield P