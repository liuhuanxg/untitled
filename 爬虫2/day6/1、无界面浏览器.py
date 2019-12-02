#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 1、无界面浏览器.py
@Time: 2019/11/29 9:27
@user：python-刘欢    
"""
from selenium import webdriver
import time

driver = webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#2、访问网站
url = 'https://www.baidu.com/'
driver.get(url=url)

#3、拍照
# driver.save_screenshot('download/baidu.png')

#4、找到输入框
driver.find_element_by_id('kw').send_keys('刘亦菲')

#5、模拟点击
driver.find_element_by_id('su').click()
time.sleep(2)
driver.save_screenshot('download/baidu3.png')