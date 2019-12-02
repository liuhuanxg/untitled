import requests
import time
import hashlib

def getMd5(values):
    md5=hashlib.md5()
    md5.update(bytes(values, encoding='utf-8'))
    return md5.hexdigest()


def request_json(word, salt, sign, ts):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        "Accept":"application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding":"gzip, deflate", #
        "Accept-Language":"zh-CN,zh;q=0.9",
        "Connection":"keep-alive",
        "Content-Length":"236",
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie":'OUTFOX_SEARCH_USER_ID_NCOO=1401138314.1523786; OUTFOX_SEARCH_USER_ID="1268946590@10.108.160.17"; _ga=GA1.2.322127542.1570845032; _ntes_nnid=5d451780b54b3e2e1c856958130c4b44,1573432972803; _gid=GA1.2.1427899356.1575006517; JSESSIONID=aaaJo6FjxV9nWdcUJU16w; ___rl__test__cookies=1575007038071',
        "Host":"fanyi.youdao.com",
        "Origin":"http://fanyi.youdao.com",
        "Referer":"http://fanyi.youdao.com/",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "X-Requested-With":"XMLHttpRequest",

    }
    data = {
        "i": word,
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":str(salt),
        "sign":str(sign),
        "ts":str(ts),
        "bv":"d49ce05a2e1d4fc492ff6bd738ecd402",
        "doctype":"json",
        "version":"2.1",
        "keyfrom":"fanyi.web",
        "action":"FY_BY_REALTlME"
    }
    response = requests.post(url=url, data=data, headers=headers).content.decode('utf-8')
    # print(response)
    return response



if __name__ == '__main__':
    word = input('请输入要翻译的单词：')
    #制造sign, salt
    salt = int(time.time()*10000)
    ts = int(time.time()*1000)
    values = "fanyideskweb" + word + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMd5(values)

    #请求：
    translate = request_json(word, salt, sign,ts)
    print(translate)
