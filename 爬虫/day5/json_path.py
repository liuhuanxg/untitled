from urllib import request
import requests
import json
import jsonpath

url='http://www.lagou.com/lbs/getAllCitySearchLabels.json'

response=request.urlopen(url)
# response=requests.get(url=url)
html=response.read()
html=html.decode('utf-8')
print(type(html),html)

#json格式字符串转换成python对象
jsonobj=json.loads(html)
print(type(jsonobj),jsonobj)