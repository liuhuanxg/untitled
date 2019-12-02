#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 2、豆瓣电影.py
@Time: 2019/11/25 11:08
@user：python-刘欢    
"""
import os
path = os.path.join(os.getcwd(),'download')
import json

import requests

url = 'https://movie.douban.com/j/chart/top_list'

headers = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Cookie':'bid=iFz9NRtk-us; douban-fav-remind=1; ll="108288"; __utmc=30149280; __utmz=30149280.1574651371.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=223695111; __utmz=223695111.1574651371.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D9AB4466392922617056B26A14DFB6715|330d0d4f71117d45d72198c3ed0c5c24; __yadk_uid=kSdTDKoiCxJqUTMASuXJLFr4VKVyHmDG; ap_v=0,6.0; __utma=30149280.490783847.1569215486.1574651371.1574661316.5; __utmb=30149280.0.10.1574661316; __utma=223695111.1080552878.1574651371.1574651371.1574661316.2; __utmb=223695111.0.10.1574661316; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1574661316%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DQRvh4w7sTfl2Jbr-O0qJlLPrYgluDIxdpPgoKHuzLCCMijihjcVgZh3V1sd39XDc%26wd%3D%26eqid%3Df8784c4f00020351000000025ddb45fd%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=28679fc2ade5b28c.1574651372.2.1574661353.1574651843.',
    'Host':'movie.douban.com',
    'Referer':'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'X-Requested-With':'XMLHttpRequestHTML',
}

params={
    'type':'11',
    'interval_id':'100:90',
    'action':'',
    'start':'0',
    'limit':'1',
}

content = requests.get(url=url,params=params,headers=headers).content.decode('utf-8')
data = json.loads(content,encoding='utf-8')
print(type(data),len(data),data)
print(data[0].get('title'))
