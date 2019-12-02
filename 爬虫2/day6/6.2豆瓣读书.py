from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
url = 'https://search.douban.com/book/subject_search?search_text=python&cat=1001'
driver.get(url=url)

#快照：
driver.save_screenshot('dushu.png')
with open('web_dushu2.html','w',encoding='utf-8')as fp:
    fp.write(driver.page_source)

#提取信息：
from lxml import etree
tree = etree.HTML(driver.page_source)
div_list = tree.xpath('//div[contains(@class,"sc-bZQynM")]')
# print(len(div_list))
for div in div_list:
    title = div.xpath('.//div[@class="title"]/a/text()')
    score = div.xpath('.//div[2]/span[2]/text()')
    comment_number = div.xpath('.//div[2]/span[3]/text()')
    public = div.xpath('.//div[3]/text()')
    print(title)
    print(score)
    print(comment_number)
    print(public)
    print('\n\n')