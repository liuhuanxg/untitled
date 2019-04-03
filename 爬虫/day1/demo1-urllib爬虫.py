from urllib import  request

#访问目标
base_url='http://www.baidu.com/'

#发起请求得到回应，得到一个对象
response=request.urlopen(url=base_url)

#读取内容并转码
content=response.read()
html=content.decode('utf-8')

#将读取的内容写入文件
with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(html)
