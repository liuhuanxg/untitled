#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo2-headers.py
@Time: 2019/11/22 10:56
@user：python-刘欢    
"""
#1、导入模块
import requests

url = 'https://www.baidu.com/s?wd=%E5%AE%8B%E7%A5%96%E5%84%BF'
#2、发起请求
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url = url,headers=headers)
print(response.encoding)

content = response.content.decode('utf-8')
print(content)

# with open('a.txt','a') as fp:
#     fp.write(content)