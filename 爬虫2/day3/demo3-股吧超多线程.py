# -*-coding:utf-8 -*-
"""
@project:untitled
@File: demo3-股吧超多线程.py
@Time: 2019/11/26 15:44
@user：python-刘欢    
"""
import re
import requests
import threading
from queue import Queue
import time


class Crawl_thread(threading.Thread):
    def __init__(self, page_queue):
        super().__init__()
        self.page_queue = page_queue

    def run(self) -> None:
        self.getContent()

    def getContent(self):
        while True:
            if self.page_queue.empty():
                break
            page = self.page_queue.get()
            url = 'http://guba.eastmoney.com/default,99_{}.html'.format(page)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            }
            content = requests.get(url=url, headers=headers).content.decode('utf-8')
            ul_pattern = re.compile(r'<ul class="newlist" tracker-eventcode="gb_xgbsy_ lbqy_rmlbdj">(.*?)</ul>', re.S)
            ul = re.findall(ul_pattern, content)[0]
            content_queue.put(ul)


class Parse_thread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        while not exitFlag:
            try:
                ul = content_queue.get(False)
                self.parseContent(ul)
            except:
                pass

    def parseContent(self, ul):
        title_pattern = re.compile(r'class="note">(.*?)</a></span>')
        title_list = re.findall(title_pattern, ul)
        result_list.append(title_list)
        ba_pattern = re.compile(r'class="balink">(.*?)</a>', re.S)
        ba_list = re.findall(ba_pattern, ul)
        zuozhe_pattern = re.compile(r'<font>(.*?)</font>', re.S)
        zuozhe_list = re.findall(zuozhe_pattern, ul)

        date_pattern = re.compile(r'<cite class="last">(.*?)</cite>', re.S)
        date_list = re.findall(date_pattern, ul)

        pinglun_pattern = re.compile(r'<li>(.*?)</li>', re.S)
        pinglun_list = re.findall(pinglun_pattern, ul)
        read_pattern = re.compile(r'<cite>(.*?)</cite>', re.S)
        for p in pinglun_list:
            data = re.findall(read_pattern, p)
            read = data[0].strip()
            pinglun = data[1].strip()

        href_pattern = re.compile('</em> <a href="(.*?)" title="')
        href_list = re.findall(href_pattern, ul)

exitFlag = False
content_queue = Queue()
result_list = []

import json
def outputFile():
    print(len(result_list))
    data = json.dumps(result_list,ensure_ascii=False)
    with open('guba1.json','w',encoding='utf-8') as fp:
        fp.write(data)


if __name__ == '__main__':
    start = time.time()
    page_queue = Queue()
    for i in range(1, 13):
        page_queue.put(i)

    #开启三个爬虫
    c_list = []
    for i in range(3):
        c = Crawl_thread(page_queue)
        c.start()
        c_list.append(c)

    #开启三个解析线程
    p_list = []
    for j in range(3):
        p = Parse_thread()
        p.start()
        p_list.append(p)

    while not page_queue.empty():
        print('爬虫还未结束！')

    for c in c_list:
        c.join()

    while not content_queue.empty():
        print('解析还未结束！')

    exitFlag = True

    for p in p_list:
        p.join()

    end = time.time()
    print(end - start)
    outputFile()