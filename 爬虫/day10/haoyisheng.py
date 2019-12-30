#-*-coding:utf-8 -*-
"""
@project:untitled
@File: haoyisheng.py
@Time: 2019/12/24 10:49
@user：python-刘欢    
"""
import requests
from lxml import etree
url = "https://www.guahao.com/publish/9df890b7-6506-4ca7-ac2f-80034db20469000/1"
response = requests.get(url)
r =response.content.decode('utf-8')

# with open("lifeng.html","a",encoding='utf-8') as fp:
#     fp.write(r)
tree = etree.HTML(r)
page = tree.xpath('//div[@class="g-pagination"]')[0]
pageNO = page.xpath('.//input[@name="pageNo"]/@value')[0]
timestamp = page.xpath('.//input[@name="timestamp"]/@value')[0]
sign = page.xpath('.//input[@name="sign"]/@value')[0]
print(int(pageNO)+1)
print(timestamp)
print(sign)


url1 = "https://www.guahao.com/publish/9df890b7-6506-4ca7-ac2f-80034db20469000/1?pageNo={}&sign={}&timestamp={}".format(int(pageNO)+1,sign,timestamp)
response = requests.get(url1)
r2 =response.content.decode('utf-8')

with open("lifeng2.html","a",encoding='utf-8') as fp:
    fp.write(r2)