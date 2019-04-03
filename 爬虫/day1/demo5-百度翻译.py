from urllib import request,parse
import json

def fanyi(word):
    header = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.106Safari / 537.36'
    }
    base_url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw':word
    }
    data_str=parse.urlencode(data)
    req=request.Request(url=base_url,headers=header,data=bytes(data_str,encoding='utf-8'))
    json_data=request.urlopen(req).read().decode('utf-8')
    dic=json.loads(json_data)
    # print(json_data)
    # print(dic)
    for word in dic['data']:
        print(word)

while True:
    if __name__ == '__main__':
        word=input('请输入要翻译的词：')
        fanyi(word)