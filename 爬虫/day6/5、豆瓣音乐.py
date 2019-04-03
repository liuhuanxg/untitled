from selenium import webdriver

#生成一个浏览器
driver=webdriver.PhantomJS(r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('https://music.douban.com/chart')

songs_list=driver.find_elements_by_xpath('//h3[@class="icon-play"]')
print(songs_list)
for songs in songs_list:
    song=songs.find_element_by_xpath('.//a')
    print(song.text)



