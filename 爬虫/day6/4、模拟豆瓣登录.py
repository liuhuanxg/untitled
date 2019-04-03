# 账号：18737307883
#密码：lgq19960425,

#引入模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import etree

#设置延迟，获取登录之后的页面
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#生成一个浏览器
driver=webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#网络请求--在浏览器的地址栏当中输入了网址，并且还按了回车
driver.get('https://www.douban.com/')

#生成当前页面快照并保存
driver.save_screenshot("index.png")

# name=input('请输入用户名：')
# password=input('请输入密码：')
driver.find_element_by_id("form_email").send_keys("18737307883")
driver.find_element_by_id("form_password").send_keys("lgq19960425,")
yanzhengma=input('请输入验证码：')
driver.find_element_by_id("captcha_field").send_keys(yanzhengma)
driver.find_element_by_class_name("bn-submit").click()

#获取新的页面快照
try:
    element=WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID,"statuses")))
    driver.save_screenshot("登录.png")
finally:
    driver.quit()


# with open('douban2.html','w',encoding='utf-8') as fp:
#     fp.write(driver.page_source)


