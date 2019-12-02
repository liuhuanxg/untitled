#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 2、链家.py
@Time: 2019/11/27 15:27
@user：python-刘欢    
"""

import requests
from lxml import etree
import re
import time


def main(url):
    content = requests.get(url=url,headers=headers).text
    a_list = etree.HTML(content).xpath('//div[@class="fc-main clear"]//a')

    for a in a_list:
        name = a.text
        get_count('https:'+a.xpath('@href')[0].strip()+'/loupan/',name)


def get_count(url,country_name):
    content = requests.get(url=url, headers=headers).text
    count = etree.HTML(content).xpath('/html/body/div[4]/div[2]/span[2]')[0].text
    items[country_name] = []
    num = int(count) // 10
    print(num)
    if  num:
        for i in range(1,num+2):
            path = url+'pg{}'.format(i)
            print(path)
            crawl_list(path,country_name)


def crawl_list(list_url,country_name):
    content = requests.get(url=list_url, headers=headers).text
    li_list = etree.HTML(content).xpath('//li[@class="resblock-list post_ulog_exposure_scroll has-results"]')
    pattern = re.compile(r'"fb_expo_id":"(.*?)"')
    for li in li_list:  #所有的房源
        item = {}
        img_src= li.xpath('./a/img')[0].xpath('@data-original')[0]
        data = li.xpath('./div[@class="resblock-desc-wrapper"]')[0]
        names = data.xpath('./div[@class="resblock-name"]')[0]
        name = names.xpath('./a')[0].text
        path = names.xpath('./a')[0].xpath('@href')[0]
        print(name)
        fb_expo_id = pattern.findall(names.xpath('./a')[0].xpath('@data-other-action')[0])
        try:
            fb_expo_id = fb_expo_id[0]
        except:
            print(fb_expo_id)
            fb_expo_id = ''
        detail_url = base_url+path+'?'+'fb_expo_id='+ fb_expo_id
        status = ','.join([i.text for i in names.xpath('./span')])
        address = data.xpath('./div[@class="resblock-location"]/span')
        add = ','.join([i.text for i in address])
        ress = data.xpath('./div[@class="resblock-location"]/a')[0].text
        area = data.xpath('./div[@class="resblock-area"]/span')[0].text
        advantages = data.xpath('./div[@class="resblock-tag"]/span')
        advantage = ''.join([a.text for a in advantages])
        prices = data.xpath('./div[@class="resblock-price"]//span')
        price =''.join([p.text.strip() for p in prices])
        try:
            total_price = data.xpath('.//div[@class="second"]')[0].text
        except:
            total_price = 'None'
        item['name'] = name
        item['img_src'] = img_src
        item['status'] = status
        item['address'] = add
        item['ress'] = ress
        item['area'] = area
        item['advantage'] = advantage
        item['price'] = price
        item['total_price'] = total_price
        items[country_name].append(item)
        crawl_detail(detail_url)
        global i
        i += 1

def crawl_detail(url):
    pass

import json
def out_File():
    with open('lianjia.json','w',encoding='utf-8') as fp:
        fp.write(json.dumps(items,ensure_ascii=False))

if __name__ == '__main__':
    i = 0
    start = time.time()
    base_url = 'https://bd.fang.lianjia.com'

    items = dict()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1:WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    main(base_url+'/loupan/')
    out_File()

    print(i)
    end = time.time()
    print(end -start)


