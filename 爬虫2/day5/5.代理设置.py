
import requests
import random

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
proxies = [{'https':'117.30.113.20:9999', 'http':'125.78.177.186:9999'},
           {'https':'122.228.19.4:3389', 'http':'117.69.201.243:9999'}]

proxy = random.choice(proxies)
print(proxy)
print(requests.get('https://www.baidu.com/', proxies=proxy))