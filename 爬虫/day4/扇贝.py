import requests
from lxml import etree
import json

# 获取页面内容
words_list = []
for i in range(1, 4):
    response = requests.get('https://www.shanbay.com/wordlist/110521/232414/?page=%s' % i)
    # print(response.text)
    seleor = etree.HTML(response.text)
    word_list = seleor.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    for word_tr in word_list:
        print(word_tr.xpath('string(.)'))
        # print()
        # word = word_tr.xpath('./td[1]/strong/text()')
        # explain = word_tr.xpath('./td[2]/text()')
        # words_list.append(word[0] + ' ' + explain[0])

with open('word.txt', 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(words_list))
