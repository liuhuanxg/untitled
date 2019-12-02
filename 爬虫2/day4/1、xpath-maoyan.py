#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 1、xpath-maoyan.py
@Time: 2019/11/27 15:08
@user：python-刘欢    
"""
import requests
import json
from lxml import etree


url = 'https://maoyan.com/board'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1:WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

response = requests.get(url=url,headers=headers).text

html = etree.HTML(response)

dl = html.xpath('//*[@id="app"]/div/div/div/dl')[0]
dd_list = dl.xpath('./dd')
for dd in dd_list:
    print(dd.xpath('./i')[0].xpath('string(.)'))
