import  requests
from lxml import etree
import json

#一：网络请求
def getContent(url):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers)

    #调用数据分析方法
    getData(response.text)

    with open('tengxun.html', 'w', encoding='utf-8') as fp:
        fp.write(response.text)


#二、数据分析
def getData(content):
    tree = etree.HTML(content)
    tr_list = tree.xpath('//table[@class="tablelist"]/tr')
    tr_list.pop()
    tr_list.pop(0)
    for td in tr_list:
        try:
            work_name = td.xpath("./td/a/text()")[0]
            work_type = td.xpath("./td/text()")[0]
            num = td.xpath("./td/text()")[1]
            place = td.xpath("./td/text()")[2]
            time = td.xpath("./td/text()")[3]
            data_info = work_name+ ',' + work_type + ',' + num + ',' + place + ',' + time + '\n'
            with open('tencent.txt', 'a', encoding='utf-8') as fp:
                fp.write(data_info)
        except:
            pass


if __name__ == '__main__':
    for page in range(1,296):
        base_url="https://hr.tencent.com/position.php?&start="
        url=base_url+str((page-1)*10)
        getContent(url)