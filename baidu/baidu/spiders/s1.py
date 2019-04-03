# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ..items import JobItem

class S1Spider(scrapy.Spider):
    name = 's1'
    allowed_domains = []
    start_urls = []
    for page in range(1, 286):
        base_url = "https://hr.tencent.com/position.php?&start="
        url = base_url + str((page - 1) * 10)

        #将路径添加到start_urls中
        start_urls.append(url)
    def parse(self, response):

        #取来数据进行解码
        content=response.body.decode('utf-8')

        tree = etree.HTML(content)
        tr_list = tree.xpath('//table[@class="tablelist"]/tr')
        tr_list.pop()
        tr_list.pop(0)

        for td in tr_list:
            try:
                title = td.xpath("./td/a/text()")[0]
                job_type = td.xpath("./td/text()")[0]
                num = td.xpath("./td/text()")[1]
                job_local = td.xpath("./td/text()")[2]
                realtime = td.xpath("./td/text()")[3]

                print(title,job_type,num,job_local,realtime)
                #使用数据模型去封装数据
                job=JobItem()
                job['title']=title
                job['job_type']=job_type
                job['num']=num
                job['job_local']=job_local
                job['realtime']=realtime

                #传输到pipelines
                yield job

            except:
                pass

