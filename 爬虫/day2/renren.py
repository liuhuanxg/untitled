from urllib import request,parse
from http import  cookiejar

cookie=cookiejar.MozillaCookieJar()
cookie_handle=request.HTTPCookieProcessor(cookie) #生成cookie管理器（处理器）

opener=request.build_opener(cookie_handle)  #自定义一个opener

def login():   #登录获取的cookie
    url='http://www.renren.com/PLogin.do'
    header={
        'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
    }
    data={
        'email': '18519020313',  # 用户名
        'password': 'hua7700969'  # 密码
    }
    data=parse.urlencode(data)
    req=request.Request(url=url,data=bytes(data,encoding='utf-8'),headers=header)
    response=opener.open(req)
    html=response.read().decode('utf-8')
    print(response.geturl())
    cookie.save('cookie.txt',ignore_expires=True,ignore_discard=True)

def getHome():
    login()
    url='http://www.renren.com/310303067/profile'
    response=opener.open(fullurl=url)
    print(response.geturl())
    html=response.read().decode('utf-8')
    print(html)

if __name__ == '__main__':
    getHome()