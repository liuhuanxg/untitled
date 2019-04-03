from lxml import etree
import requests
import re

for i in range(1,4):
    base_url='https://www.shanbay.com/wordlist/110521/232414/?page=%s'%i
    header={
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    }

    response=requests.get(url=base_url,headers=header)
    html=etree.HTML(response.text)
    words = html.xpath('//td[@class="span2"]/strong/text()')
    fanyi = html.xpath('//td[@class="span10"]/text()')
    j=0
    while j <len(words):
        list=fanyi[j].split()
        with open('python常用单词.txt','a+',encoding='utf-8') as fp:
             fp.write(words[j]+'         ')
        for s in list:
            with open('python常用单词.txt', 'a+', encoding='utf-8') as fp:
                fp.write(s)
        with open('python常用单词.txt', 'a+', encoding='utf-8') as fp:
            fp.write('\n')
        j+=1