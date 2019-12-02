#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 2、有道翻译.py
@Time: 2019/11/29 14:01
@user：python-刘欢    
"""
import requests
import time
import hashlib

def main():
    response = requests.post(url=url,data=data)
    print(response.text)

def getMd5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value),encoding='utf-8')
    return md5.hexgiest()
if __name__ == '__main__':
    while True:
        salt = str(time.time()*10000).split('.')[0]
        i = input("请输入字符：")
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        value = 'fanyideskweb'+ i + salt + 'n%A-rKaT5fb[Gy?;N5@TG'
        sign = getMd5(value)
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 'Accept-Encoding':'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '238',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID_NCOO=1262783704.4217014; OUTFOX_SEARCH_USER_ID="-763681285@10.108.160.18"; _ga=GA1.2.1779775080.1568725575; _gid=GA1.2.191040510.1574928802; JSESSIONID=aaaoXsoMrh4Ex9RZKW16w; ___rl__test__cookies=1575007487620',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {
            'i': i,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': salt,
            'sign': sign,
            'ts': salt[:-1],
            'bv': 'f0325f69e46de1422e85dedc4bd3c11f',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }

        main()
