#-*-coding:utf-8 -*-
"""
'@project':'untitled'
'@File':' 1、session.py'
'@Time':' 2019/11/25 10:18'
@user：python-刘欢
"""
import requests
url = 'http://www.renren.com/PLogin.do'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

data = {
    'email':18737307883,
    'password':'lh426425,'
}

#两种方式模拟登录：
#1、在headers中添加cookie值
#2、使用request.session()登录

#1、实例化session对象
session = requests.session()

#2、发起一个请求
session.post(url=url,headers=headers,data=data)


#3、访问首页信息
'''
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding':'gzip,deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'anonymid=k39t01xw-mbb1mn; depovince=BJ; _r01_=1; jebe_key=2068b70c-c1d4-412f-8a0a-d8fbbdfcf197%7Cdadddc6035a1b6107f2de248636b7900%7C1574406547830%7C1%7C1574406524286; ln_uact=18737307883; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=7f985238-2afa-4cbd-9860-0c7f671a431f|||||; JSESSIONID=abcdgmqpf5Izo4nXbxG6w; ick_login=74f27e59-fe28-47ef-bb50-3e0a62a96fd2; _de=3779F68F75A82E2BD4C1E1D152C27C5B; p=91a226fe84bb637de694b5018cc149d13; first_login_flag=1; t=93e93a3651a17c86379988c481f6829a3; societyguester=93e93a3651a17c86379988c481f6829a3; id=968459163; xnsid=5fa3c251; ver=7.0; loginfrom=null; wp_fold=0; jebe_key=2068b70c-c1d4-412f-8a0a-d8fbbdfcf197%7C956960779d820da9120b3513c88b7528%7C1574648637660%7C1%7C1574648612259',
    'Host':'www.renren.com',
    'Referer':'http://www.renren.com/968459163',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
'''
url = 'http://www.renren.com/968459163/profile'
content = session.get(url=url,).content.decode('utf-8')

print(content)
