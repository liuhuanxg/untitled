import requests
from lxml import etree
import threading
from queue import Queue
import json

#定义两个类，一个请求数据，一个解析数据


#建立两个队列，一个用来存储路由
class Get_url(threading.Thread):
    def __init__(self,page_queue):
        threading.Thread.__init__(self)
        self.page_queue=page_queue
    def run(self):
        self.getdata()
    def getdata(self):
        #设置一个死循环，不断地去爬取数据
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        while True:
            if self.page_queue.empty():
                break
            try:
                page=page_queue.get()
                url='https://hr.tencent.com/position.php?start=' + str((page - 1) * 10)
                response=requests.get(url=url,headers=headers)
                parse_queue.put(response.text)

            except:
                pass

#一个用来解析获取的数据
class Parse_data(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #从待解析队列里取数据
        while True:
            if  exitFlag:
                break
            try:
                #强取
                content=parse_queue.get(False)
                self.parsedata(content)
            except:
                pass
    def parsedata(self,content):
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
                data_list.append(item)
            except:pass


#写一个方法，用来储存数据
def save_data():
    data=json.dumps(data_list,ensure_ascii=False)
    with open('test.txt','a',encoding='utf-8')as fp:
        fp.write(data)

#建立一个解析数据队列
parse_queue=Queue()

#设置一个标志位，控制数据解析
exitFlag=False

data_list=[]

if __name__ == '__main__':
   #先创建任务队列
    page_queue=Queue()
    for page in range(295):
        page_queue.put(page)


    #开启三个爬虫，不断地爬取数据
    craw_list=[]
    for i in range(3):
        t=Get_url(page_queue)
        t.start()
        craw_list.append(t)

    # 建立线程，去处理数据
    parse_list = []
    for i in range(3):
        t = Parse_data()
        t.start()
        parse_list.append(t)

    # 当任务路径没有解析完成时候
    while not page_queue.empty():
        print('还有数据！')
        pass

    #最后一个任务完成就进入阻塞状态
    for t in craw_list:
        t.join()
    #当执行到这，代表任务路径已经处理完成
    #剩下的就是解析数据

    while not parse_queue.empty():
        print('还有任务！')
        pass

    #当执行到这的时候，代表所有任务都处理完了，可以下班了
    exitFlag = True

    # 最后一个任务完成就进入阻塞状态
    for t in parse_list:
        t.join()

    #最后的存储数据操作
    print('存储数据....')
    save_data()

