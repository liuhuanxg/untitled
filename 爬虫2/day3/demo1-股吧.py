#-*-coding:utf-8 -*-
"""
@project:untitled
@File: demo1-股吧.py
@Time: 2019/11/26 10:32
@user：python-刘欢    
"""
import os
import json
import requests
import threading
import re
import time

start_time = time.time()

for page in range(1,13):
    url = 'http://guba.eastmoney.com/default,99_{}.html'.format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
    }
    content = requests.get(url=url, headers=headers).content.decode('utf-8')
    ul_pattern = re.compile(r'<ul class="newlist" tracker-eventcode="gb_xgbsy_ lbqy_rmlbdj">(.*?)</ul>', re.S)
    ul = re.findall(ul_pattern, content)[0]

    title_pattern = re.compile(r'class="note">(.*?)</a></span>')
    title_list = re.findall(title_pattern, ul)
    print(len(title_list), title_list)

    ba_pattern = re.compile(r'class="balink">(.*?)</a>', re.S)
    ba_list = re.findall(ba_pattern, ul)
    print(len(ba_list), ba_list)
    zuozhe_pattern = re.compile(r'<font>(.*?)</font>', re.S)
    zuozhe_list = re.findall(zuozhe_pattern, ul)
    print(len(zuozhe_list), zuozhe_list)

    date_pattern = re.compile(r'<cite class="last">(.*?)</cite>', re.S)
    date_list = re.findall(date_pattern, ul)
    print(len(date_list), date_list)

    pinglun_pattern = re.compile(r'<li>(.*?)</li>', re.S)
    pinglun_list = re.findall(pinglun_pattern, ul)
    read_pattern = re.compile(r'<cite>(.*?)</cite>', re.S)
    for p in pinglun_list:
        data = re.findall(read_pattern, p)
        read = data[0].strip()
        pinglun = data[1].strip()
        print(read, pinglun)

    href_pattern = re.compile('</em> <a href="(.*?)" title="')
    href_list = re.findall(href_pattern, ul)
    print(href_list)
print(time.time()-start_time)