#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo6-人人网.py
@Time: 2019/11/22 15:21
@user：python-刘欢    
"""
import requests
url = 'http://www.renren.com/PLogin.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

data = {
    'email':18737307883,
    'password':'lh426425,'
}
response = requests.post(url=url,data=data,headers=headers)
content = response.content.decode('utf-8')
print(content)