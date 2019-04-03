# http://www.runoob.com/python/python-exercise-example1.html
import requests
from lxml import etree
import os
def Pati(url):
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    response=requests.get(url=url,headers=header)
    response.encoding='utf-8'
    tree=etree.HTML(response.text)
    Div=tree.xpath('//div[@id="content"]')
    #名字
    h=Div[0].xpath('./h1//text()')[0]
    if h != ' ':
        name=h.split(' ')[1]
    #题目
    Timu = Div[0].xpath('./p[2]')[0]
    if Timu !=' ':
        timu=Timu.xpath('string(.)')
    #分析
    Fenxi = Div[0].xpath('./p[3]')[0]
    fenxi=Fenxi.xpath('string(.)')

    #题目具体
    try:
        div=Div[0].xpath('//div[@class="hl-main"]')
        info=div[0].xpath('string(.)')
        # 答案
        pre = Div[0].xpath('./pre[1]')
        pre_info = pre[0].xpath('string(.)')

    except:
        div = Div[0].xpath('./pre[1]')
        info = div[0].xpath('string(.)')
        pre = Div[0].xpath('./pre[2]')
        pre_info = pre[0].xpath('string(.)')
    # 路径
    mz = os.getcwd() + '\\' + '100题' + '\\'
    #内容
    s = "'''" + timu + '\n' + fenxi + '\n' + "'''"+'\n' + "'''" + info +'\n'+ "'''" + '\n' + "'''" + pre_info + "'''"
    with open(mz + name + '.py', 'a', encoding='utf-8') as fp:
        fp.write(s)


if __name__ == '__main__':
    for i in range(1,101):
        url='http://www.runoob.com/python/python-exercise-example%d.html'%i
        Pati(url)
