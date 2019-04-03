import threading
import requests
from lxml import etree
from queue import Queue
import json


#网络请求线程类
class Crawl_Thread(threading.Thread):

    def __init__(self,page_queue):
        threading.Thread.__init__(self)
        self.page_queue=page_queue

    def run(self):
        self.getContent()

    #一、网络请求
    def getContent(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }

        #用死循环不停的去访问队列
        while True:
            if self.page_queue.empty(): #当任务队列为空，就退出
                break

            #从任务队列当中取页码
            page=self.page_queue.get()

            #生成对应的url
            url = 'https://hr.tencent.com/position.php?start=' + str((page - 1) * 10)

            #发起请求
            response=requests.get(url,headers=headers)
            content_queue.put(response.text)


#数据解析线程
class Parse_Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while not exitFlag:  # 退出线程
            try:
                # 从队列中提取数据
                content = content_queue.get(False)

                # 调用数据解析方法
                self.getData(content)
            except:
                pass
    #数据解析
    def getData(self, content):
        tree = etree.HTML(content)
        tr_list = tree.xpath('//table[@class="tablelist"]/tr')
        tr_list.pop()  # 去尾
        tr_list.pop(0)  # 去头

        for tr in tr_list:
            try:
                title = tr.xpath('./td/a/text()')
                job_type = tr.xpath('./td/text()')[0]
                num = tr.xpath('./td/text()')[1]
                local = tr.xpath('./td/text()')[2]
                realtime = tr.xpath('./td/text()')[3]

                # 格式化数据
                item = {}
                item['title'] = title[0]
                item['job_type'] = job_type
                item['num'] = num
                item['local'] = local
                item['realtime'] = realtime

                # 将每一个职位信息当成一个元素，追加到job_list列表当中
                job_list.append(item)

            except:
                pass

#序列化文件（内存信息，文件两之间的操作叫~~~）
def output2File():
    data = json.dumps(job_list,ensure_ascii=False)

    #一次性完成所有数据的插入操作
    with open('tencent.txt', 'w', encoding='utf-8') as fp:
        fp.write(data,)

#页面内容列表
job_list=[]

#页面内容队列
content_queue=Queue()

exitFlag=False  #默认不退出

if __name__ == '__main__':

    #创建一个任务队列
    page_queue=Queue()  #默认不限定任务个数
    for page in range(295):
        page_queue.put(page)

    #开启三个爬虫，不断地爬取数据
    crawl_list=[]
    for i in range(3):
        t=Crawl_Thread(page_queue)
        t.start()
        crawl_list.append(t)

    #三个解析线程
    parse_list=[]
    for i in range(0,3):
        parse_t=Parse_Thread()
        parse_t.start()
        parse_list.append(parse_t)


    #等待所有任务都完成
    while not page_queue.empty():
        print('请求队列中还有任务！')
        pass

    #网络请求阻塞
    for t in crawl_list:
        t.join()

    #执行到这里，说明网络请求线程全部结束

    #页面队列为空
    while not content_queue.empty():
        print('页面队列中还有任务！')
        pass

    #执行到这里，说明页面队列为空
    #两个条件都具备，则允许数据解析线程退出
    exitFlag=True

    # 阻塞
    for parse_t in parse_list:
        parse_t.join()


    #存储数据
    print('开始序列化。。。')
    output2File()


