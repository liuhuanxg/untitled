#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo7.py
@Time: 2019/11/22 16:38
@user：python-刘欢    
"""
import requests
url = 'http://fy.iciba.com/ajax.php?a=fy'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
data = {
    'w':'hello'
}
response = requests.post(url=url,data=data,headers=headers)
content = response.content.decode('utf-8')
import json
content = json.loads(content)
word_list = content['content']['word_mean']
with open('hello.txt', 'a+') as fp:
    fp.write('hello\r')
for i in word_list:
    with open('hello.txt', 'a+',encoding='utf8') as fp:
        fp.write(i+'\r')