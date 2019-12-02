from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'd:\Desktop\chromedriver_win32\chromedriver.exe')

driver.get('https://www.baidu.com/')

driver.find_element_by_id('kw').send_keys('杨超越')

# import time
# time.sleep(1)
# driver.find_element_by_id('su').click()

#===========模拟快捷键操作：=======================================
from selenium.webdriver.common.keys import Keys
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# driver.save_screenshot('qx.png')
#
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
# driver.save_screenshot('jq.png')
#
# driver.find_element_by_id('kw').send_keys('赵四')
# driver.find_element_by_id('su').click()

driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
# driver.find_element_by_id('kw').send_keys('赵四')
# driver.find_element_by_id('su').click()

driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)
driver.find_element_by_id('kw').send_keys('赵四')
