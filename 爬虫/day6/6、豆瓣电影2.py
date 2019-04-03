from selenium import webdriver
import time

import requests

url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
# response = requests.get(url)
# with open('douban.html','w',encoding='utf-8') as fp:
#     fp.write(response.text)

#生成一个浏览器
driver = webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#网络请问
driver.get(url)
driver.save_screenshot('douban02.png')#此时只有前20部电影

js = 'document.body.scrollTop=10000'
driver.execute_script(js)
time.sleep(3)
driver.save_screenshot('douban03.png')
