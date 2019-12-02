from selenium import webdriver
import time

#(1)将selenium和浏览器组合：
driver = webdriver.PhantomJS(executable_path=r'd:\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#(2)访问网站;
url='https://www.baidu.com/'
driver.get(url=url)

#(3).拍照：
driver.save_screenshot('baidu01.png')

#(4)#找到输入框, 模拟输入：
driver.find_element_by_id('kw').send_keys('杨超越')

#(5)拍照：
driver.save_screenshot('baidu02.png')

# with open('baidu.html','w',encoding='utf-8')as fp:
#     fp.write(driver.page_source)

#(6)模拟点击：
driver.find_element_by_id('su').click()
time.sleep(2)
driver.save_screenshot('baidu03.png')