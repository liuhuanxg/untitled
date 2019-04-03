#引入模块
from selenium import webdriver
from lxml import etree

#生成一个浏览器
driver=webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#网络请求--在浏览器的地址栏当中输入了网址，并且还按了回车
driver.get('https://book.douban.com/subject_search?search_text=python&cat=1001')

#页面内容---字符串
# driver.page_source
with open('douban02.html','w',encoding='utf-8') as fp:
    fp.write(driver.page_source)

#提取数据
from lxml import etree

tree=etree.HTML(driver.page_source)
books=tree.xpath('//div[@class="item-root"]')

for book in books:
    title=book.xpath('./div[@class="detail"]/div[@class="title"]/a/text()')
    detail=book.xpath('./div[@class="detail"]/div[@class="meta abstract"]/text()')

    #链接
    link = book.xpath('./div[@class="detail"]/div[@class="title"]/a/@href')
    print(title,detail,link)
