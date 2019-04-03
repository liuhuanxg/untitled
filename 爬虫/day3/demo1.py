import requests

# r=requests.get('https://api.github.com/events')
#
# r=requests.post('http://httpbin.org/post', data = {'key':'value'})
#
# r=requests.put('http://httpbin.org/put')
# r=requests.delete('http://httpbin.org/delete')
# r=requests.head('http://httpbin.org/head')
# r=requests.options('http://httpbin.org/options')
# print(r.text)

# payload={'key1':'value1','key2':'value2'}
# r=requests.get("http://httpbin.org/get", params=payload)
# print(r.text)
# print(r.url)

# payload={'key1':'value1','key2':['value2','value3']}
# r=requests.get('http://httpbin.org/get',params=payload)
# print(r.url)

r=requests.get('https://www.zhihu.com')
print(r.text)