from selenium import webdriver
import time
driver = webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'http://fanyi.youdao.com/'

driver.get(url=url)
driver.save_screenshot('yd1.png')
driver.find_element_by_id('inputOriginal').send_keys('work')

# driver.find_element_by_id()
time.sleep(2)
driver.save_screenshot('yd2.png')

with open('youdao.html', 'w', encoding='utf-8')as fp:
    fp.write(driver.page_source)

from lxml import etree

tree = etree.HTML(driver.page_source)
fanyi = tree.xpath('//div[@class="dict__relative"]//span/text()')
print(fanyi)