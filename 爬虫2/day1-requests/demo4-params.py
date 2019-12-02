#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo4-params.py
@Time: 2019/11/22 14:00
@user：python-刘欢    
"""

import os
import requests
def search(url):
    path = os.path.join(os.getcwd(), 'download/demo4-tieba.html')
    params = {
        'kw': 'java',
        'ie': 'utf-8',
        'pn': 50,
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers,params=params)
    content = response.content.decode('utf-8')
    with open(path,'w',encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    url = 'http://tieba.baidu.com/f?'
    search(url)
