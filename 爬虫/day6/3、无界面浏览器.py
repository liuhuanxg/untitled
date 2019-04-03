#引入模块
from selenium import webdriver
import time

#生成一个浏览器
driver=webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#网络请求
driver.get('http://www.baidu.com')

#截屏
driver.save_screenshot('baidu01.png')

#模拟用户输入
driver.find_element_by_id('kw').send_keys("优就业")

driver.save_screenshot('baidu02.png')

#模拟用户点击搜索
driver.find_element_by_id('su').submit()

start_time=time.time()

#模拟用户点击按钮
# driver.find_element_by_id('su').submit()
#
# start_time = time.time()
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "content_left"))
#     )
#     driver.save_screenshot('baidu03.png')
#     end_time = time.time()
#
#     print("通信所有时间为：",end_time-start_time)
# finally:
#     driver.quit()

#获取cookies
print(driver.get_cookies())

#模拟全选操作---ctrl+a
from selenium.webdriver.common.keys import Keys
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.save_screenshot('baidu04.png')

#获取url
print(driver.current_url)

#获取文字内容和属性
driver.get('https://book.douban.com/subject_search?search_text=python&cat=1001')
books = driver.find_elements_by_xpath('//div[@class="item-root"]')
for book in books:
    a = book.find_element_by_xpath('.//div[@class="title"]/a')
    #属性
    detail_url = a.get_attribute('href')
    #文字
    book_name = a.text
    print(book_name,detail_url)
