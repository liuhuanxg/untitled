import requests
from lxml import etree

def xiaomi(url):
    response=requests.get(url=url)
    response.encoding='utf-8'
    with open('xiaomi.html','a',encoding='utf-8')as fp:
        fp.write(response.text)
    tree=etree.HTML(response.text)
    title_list=tree.xpath('//span[@class="name"]/text()')
    print(title_list)
if __name__ == '__main__':
    url='https://www.mi.com/seckill/'
    xiaomi(url)