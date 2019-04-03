#为了更高效率地爬取数据，使用多线程
import requests
from lxml import etree
#导入线程包
import threading
import json

class Crawl_Thread(threading.Thread):

    def __init__(self,page):
        threading.Thread.__init__(self)
        self.page=page

    #线程类必须复写run方法，从run方法开始执行
    def run(self):
        self.getContent()

    #一、网络请求
    def getContent(self,):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        url = 'https://hr.tencent.com/position.php?start=' + str((self.page - 1) * 10)

        response = requests.get(url=url, headers=headers)

        self.getData(response.text)

    #二、数据解析
    def getData(self,content):
        tree = etree.HTML(content)
        tr_list = tree.xpath('//table[@class="tablelist"]/tr')
        tr_list.pop()
        tr_list.pop(0)
        for td in tr_list:
            try:
                data = {}
                work_name = td.xpath("./td/a/text()")
                work_type = td.xpath("./td/text()")[0]
                num = td.xpath("./td/text()")[1]
                place = td.xpath("./td/text()")[2]
                time = td.xpath("./td/text()")[3]
                data['职位名称'] = work_name
                data['职位类别'] = work_type
                data['人数'] = num
                data['地点'] = place
                data['发布时间'] = time
                # print(work_name,work_type,num,place,time)

                shuju=json.dumps(data,ensure_ascii=False)
                with lock:
                    with open('tengxun.txt', 'a', encoding='utf-8') as fp:
                        fp.write(shuju + '\n')
            except:
                  pass

#进程锁
lock=threading.Lock()

if __name__ == '__main__':
    for page in range(1,200):
        t=Crawl_Thread(page)
        t.start()