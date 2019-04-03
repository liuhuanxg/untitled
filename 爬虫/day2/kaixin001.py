from urllib import request,parse
from http import cookiejar
import ssl

ssl._create_default_https_context=ssl._create_unverified_context
#关闭ssl验证

cookie=cookiejar.LWPCookieJar()
http_handle=request.HTTPHandler(debuglevel=1)
cookie_handle=request.HTTPCookieProcessor(cookie)
opener=request.build_opener(cookie_handle,http_handle)
url='https://security.kaixin001.com/login/login_auth.php'

header={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '85',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_ref=5bcec45391e22; _vid=C83086272AE0000139CA640310401870',
    'Host': 'security.kaixin001.com',
    'Origin': 'http://login.kaixin001.com',
    'Referer': 'http://login.kaixin001.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
}
data={
    'rcode':'',
    'url':'17851728219',
    'password': 'wgq123.',
    'code': ''
}
data=parse.urlencode(data)
req=request.Request(url=url ,data=bytes(data,encoding='utf-8'),headers=header)
req.add_header('Accept-Language', 'zh-CN,zh;q=0.9')
req.headers
response=opener.open(req)
request.urlopen(url=url)

print(response.read().decode('utf-8'))
response.geturl()

cookie.save('kaixin_cookie.txt',ignore_expires=True,ignore_discard=True)

response_home=opener.open('http://www.kaixin001.com/home/index.php')
