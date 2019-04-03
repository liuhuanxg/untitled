from urllib import request,parse
from  http import cookiejar   # CookieJar -> FileCookieJar  -> (MozillaCookieJar   LwpCookieJar)

cookie=cookiejar.MozillaCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)  #将cookie文件内的内容重新加载

cookie_handle=request.HTTPCookieProcessor(cookie)  #生成cookie管理器(处理器)

opener=request.build_opener(cookie_handle)   #自定义一个opener

for item in cookie:
    print(item.__dict__)

response=opener.open('http://www.renren.com/310303067/profile')
html=response.read().decode('utf-8')
print(html)
