from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.action_chains import ActionChains
# 定位 添加条件 按钮，经观需要鼠标悬停

#生成一个浏览器
driver=webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

#访问网址
driver.get("https://music.163.com/")

# try:
#     driver.find_element_by_class_name('m-tophead f-pr j-tflag').move_to_element()
#     print('1')
# finally:
#     driver.quit()

xpath_button_add_condition = '//div[@class="m-tophead f-pr j-tflag"]/a[contains(text())]'

move_on_to_add_condition = driver.find_element_by_xpath(xpath_button_add_condition)
ActionChains(driver).move_to_element(move_on_to_add_condition).perform()

driver.save_screenshot('wyy.png')



# driver.save_screenshot('wyy.png')