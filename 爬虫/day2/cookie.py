from urllib import request,parse
from  http import cookiejar   # CookieJar -> FileCookieJar  -> (MozillaCookieJar   LwpCookieJar)

# cookie = cookiejar.CookieJar()  # 实例化CookieJar 用来保存cookie
cookie=cookiejar.MozillaCookieJar()
cookie_handle=request.HTTPCookieProcessor(cookie)  #生成cookie管理器（处理器）
opener=request.build_opener(cookie_handle)  #自定义一个 opener

# url = 'http://www.renren.com/PLogin.do'
url = 'http://www.langlang2017.com/route.do'
header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'
}
data={
    'email': '18519020313',  # 用户名
    'password': 'hua7700969'  # 密码
}

data=parse.urlencode(data)
req=request.Request(url=url,data=bytes(data,encoding='utf-8'),headers=header)

# req.add_header('Host', 'www.renren.com')  # 添加一个请求头
# print('User-Agent:', req.get_header('User-agent'))
# add_header ,get_header ，headers
# print(req.headers)

# response = request.urlopen(url=req)
response=opener.open(req)

# print(response.info())
# print(response.geturl())

html=response.read().decode('utf-8')
print(html)

# for item in cookie:
#     print(item.__dict__)
# print(item.name)
# print(item.value)

cookie.save('cookie3.txt')

# home_response = opener.open('http://www.renren.com/310303067/profile')
# html = home_response.read().decode('utf-8')
# print(html)