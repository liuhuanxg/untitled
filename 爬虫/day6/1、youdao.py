import requests
import time,random,hashlib
import json

#需要翻译的内容
kw=input('请输入需要翻译的单词：')

#时间戳
salt=str(int(time.time()*1000)+random.randint(0,10))  #加盐

#sign
content="fanyideskweb"+kw+salt+"6x(ZHw]mwzX#u0V7@yfwK"

def getMd5(value):
        md5 = hashlib.md5()
        md5.update(value.encode('utf-8'))
        result = md5.hexdigest()
        return result
sign = getMd5(content)


#网址
base_url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

headers={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Connection':'keep-alive',
        'Content-Length':str(196+len(kw)),
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'OUTFOX_SEARCH_USER_ID=909058178@114.253.0.69; OUTFOX_SEARCH_USER_ID_NCOO=586693227.1349227; JSESSIONID=aaa_RrbBwabWV696lL9Aw; ___rl__test__cookies=1540779680731',
        'Host':'fanyi.youdao.com',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
}

data={
        'i':kw,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTIME',
        'typoResult':'false',
}

response=requests.post(url=base_url,headers=headers,data=data)
s=response.text
k=json.loads(s)
for i in k['smartResult']['entries']:
        print(i)