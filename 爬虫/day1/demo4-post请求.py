from urllib import request,parse
import json
keyword=input('请输入要翻译的单词：')
header = {
    'User-Agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 68.0.3440.106Safari / 537.36'
}
data={
    'kw':keyword
}
data=parse.urlencode(data)
base_url='https://fanyi.baidu.com/sug'
req=request.Request(url=base_url,headers=header,data=bytes(data.encode('utf-8')))
html=request.urlopen(req).read().decode('utf-8')
content=json.loads(html)
print(content)