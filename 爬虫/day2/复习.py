from urllib import request, parse

# 定一个URL
url = 'http://tieba.baidu.com/f?'  # ?ie=&kw=Python&fr=search&red_tag=b0100774320

data = {
    # 'ie':'utf-8',
    'kw': 'C',
    # 'fr':'search',
    # 'red_tag':'b0100774320',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'
}
data = parse.urlencode(data)

# 打开这个链接并得到响应
# response = request.urlopen(url + data)
# response = request.urlopen(url, data=bytes(data, encoding='utf-8'), timeout=10)
req = request.Request(url=url, data=bytes(data, encoding='utf-8'), headers=header)
response = request.urlopen(url=req)

# 得到页面内容 ，read().decode()
html = response.read().decode('utf-8')
print(html)


# 178 5172 8219
# wgq123.