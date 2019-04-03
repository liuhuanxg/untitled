# 导入包
from urllib import request, parse
from http import cookiejar  # CookieJar -> FileCookieJar  -> (MozillaCookieJar   LwpCookieJar)
import ssl

# cookie = cookiejar.CookieJar()  # 实例化CookieJar 用来保存cookie
cookie = cookiejar.MozillaCookieJar()
cookie_handle = request.HTTPCookieProcessor(cookie)  # 生成 cookie 管理器(处理器)
https_handle = request.HTTPSHandler()
http_handle = request.HTTPHandler()
opener = request.build_opener(cookie_handle, https_handle, http_handle)  # 自定义一个 opener

url = 'https://www.github.com'

# ssl._create_default_https_context = ssl._create_unverified_context

# url = 'https://www.12306.cn'
response = request.urlopen(url)
# response = opener.open(fullurl=url)
html = response.read().decode('utf-8')

with open('12306.html', 'w', encoding='utf-8') as fp:
    fp.write(html)

# "fanyideskweb" + 查询的词 + t + "6x(ZHw]mwzX#u0V7@yfwK"