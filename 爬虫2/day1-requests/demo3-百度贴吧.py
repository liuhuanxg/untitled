#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo3-百度贴吧.py
@Time: 2019/11/22 11:12
@user：python-刘欢    
"""
#http://tieba.baidu.com/f?ie=utf-8&kw=python
#http://tieba.baidu.com/f?ie=utf-8&kw=java
import os
path =os.path.join(os.getcwd(),'download/tieba.html')

print(path)
import requests
def search(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    content = response.content.decode('utf-8')
    with open(path,'w',encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    kw = input('请输入关键字：')
    pn = int(input("请输入页码："))
    url = 'http://tieba.baidu.com/f?ie=utf-8&kw={}&pn={}'.format(kw,pn)
    search(url)

