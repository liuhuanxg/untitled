import requests
import json
import re

##
url_list = [
'https://tce.taobao.com/api/mget.htm?callback=jsonp2127&tce_sid=1870343,1871658&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
'https://tce.taobao.com/api/mget.htm?callback=jsonp1953&tce_sid=1870341,1871659&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',

'https://tce.taobao.com/api/mget.htm?callback=jsonp2040&tce_sid=1870342,1871657&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
'https://tce.taobao.com/api/mget.htm?callback=jsonp1866&tce_sid=1870340,1871656&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
'https://tce.taobao.com/api/mget.htm?callback=jsonp1779&tce_sid=1870333,1871655&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
'https://tce.taobao.com/api/mget.htm?callback=jsonp1692&tce_sid=1870321,1871654&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
'https://tce.taobao.com/api/mget.htm?callback=jsonp1605&tce_sid=1870316,1871653&tce_vid=2,2&tid=,&tab=,&topic=,&count=,&env=online,online',
'https://tce.taobao.com/api/mget.htm?callback=jsonp1401&tce_sid=1870299&tce_vid=1&tid=&tab=&topic=&count=&env=online'
]

for i, url in enumerate(url_list):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    response = requests.get(url=url, headers=headers).content.decode('utf-8')
    # with open(f'taobao{i}.json','w',encoding='utf-8')as fp:
    #     fp.write(response)

    #解析,提取标准json格式：
    pattern = re.compile(r'\(\s+(.*?)\s+\)',re.S)
    # pattern = re.compile(r'(\{.*\})')
    response_json = pattern.findall(response)[0]
    print(response_json)

    #json转python：
    data = json.loads(response_json)

    #键获取：
    key_pattern = re.compile(r'tce_sid=(\d+)')
    key = key_pattern.findall(url)[0]
    print(key)

    data_list = data["result"][key]["result"]
    print(data_list)

    for product in data_list:
        item_current_price = product['item_current_price']
        item_pic = 'http:' + product['item_pic']
        item_title = product['item_title']
        item_url = 'https:'+ product['item_url']

        print(item_title)
        print(item_current_price)
        print(item_pic)
        print(item_url)
        print('\n')












