from urllib import request, parse
import urllib
import random

list=[
    {'http': '119.180.168.81:8060'},
    {'http': '95.64.253.77:53222'},
    {'http': '140.227.79.108:3128'},
    {'http': '121.31.63.27:39734'},
    {'http': '39.105.95.204'},
    {'http': '110.40.13.5'},
]
proxy_handle=request.ProxyHandler(random.choice(list))  #代理的处理器
http_handle=request.HTTPHandler()
opener=request.build_opener(http_handle)
url='http://www.langlang2017.com/index1.html'
header = {
    # 'Accept': ' application/json, text/javascript, */*; q=0.01',
    # 'Accept-Encoding': ' gzip, deflate',
    # 'Accept-Language': ' zh-CN,zh;q=0.9',
    # 'Connection': ' keep-alive',
    # 'Content-Length': ' 200',
    # 'Content-Type': ' application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': ' P_INFO=xt_study; _ga=GA1.2.1390003188.1539939825; OUTFOX_SEARCH_USER_ID_NCOO=968228487.9461423; OUTFOX_SEARCH_USER_ID="-1247069388@10.168.11.12"; _ntes_nnid=75c503485f4b66b6b4d3881a0775c985,1540168395984; JSESSIONID=aaanKRwZZ4dzxfKw5WFAw; ___rl__test__cookies=1540279317587',
    # 'Host': ' fanyi.youdao.com',
    # 'Origin': 'http://fanyi.youdao.com',
    # 'Referer': 'http://fanyi.youdao.com/',
    'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
    # 'X-Requested-With': ' XMLHttpRequest',
}
data = {
    # 'i': ' word',
    # 'from': ' AUTO',
    # 'to': ' AUTO',
    # 'smartresult': ' dict',
    # 'client': ' fanyideskweb',
    # 'salt': ' 1540279317593',
    # 'sign': ' dbc6efc687bb02d9c6e754cd84f8c2a2',
    # 'doctype': ' json',
    # 'version': ' 2.1',
    # 'keyfrom': ' fanyi.web',
    # 'action': ' FY_BY_REALTIME',
    # 'typoResult': ' false',
}
data = parse.urlencode(data)
req = request.Request(url=url, data=bytes(data, encoding='utf-8'), headers=header)
# response = request.urlopen(req, timeout=10)
try:
    response = opener.open(req)
except urllib.error.URLError as e:
    print(e)
except urllib.error.HTTPError as e:
    print(e)

# URLError
# print(response.read().decode())
