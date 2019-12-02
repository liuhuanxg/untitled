#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo1-requestst.py
@Time: 2019/11/22 9:30
@user：python-刘欢
"""

#1、导入模块
import requests


url = 'https://www.baidu.com/'
# https://www.baidu.com/s?wd=%E5%AE%8B%E7%A5%96%E5%84%BF
#2、发起请求
response = requests.get(url = url)
print(response)


content = response.content.decode('utf-8')
print(content)

with open('a.txt','a') as fp:
    fp.write(content)