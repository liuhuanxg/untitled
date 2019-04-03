import jsonpath
import json

#json字符串通过json.loads()转化成python对象，
#字符串转化为列表
'''
strList='[1,2,3,4]'
data=json.loads(strList)
print(type(strList),strList)
print(type(data),data)
for i in strList:
    print(i,end=' ',)

for j in data:
    print(j,end=' ')
'''

#字符串类型转化为字典
'''
strdic='{"name":"郎朗渔家","tell":"13838738789"}'
data=json.loads(strdic)
print(type(strdic),strdic)
print(type(data),data)
for i in strdic:
    print(i,end='')

#遍历字典的键
for key in data:
    print(key,end='')
'''

#非标准格式的转化,数字会转化为int
'''
str='123'
data=json.loads(str)
print(type(str),str)
print(type(data),data)
'''

#汉字进行转化会报错
'''
str='郎朗'
try:
    data=json.loads(str)
    print(type(data),data)
except:
    print('操作有误！')
'''

# json.dumps()将python对象转化为json数据
#列表转化
'''
list=[1,2,3,4]
str=json.dumps(list)
print(type(str),str)
'''

#元组
'''
tuple1=('a','b','c','d')
str=json.dumps(tuple1)
print(type(str),str)
'''

#字典
'''
dict={"name":"郎朗渔家",'tell':'123344'}
#json.dumps()序列化时默认使用ascii编码，ensure_ascii=False不进行转码
data=json.dumps(dict,ensure_ascii=False)
print(type(data),data)
'''

#json.dump()写到文件
'''
dict={"name":"郎朗渔家",'tell':'123344'}
list=["乘船出海","赶海垂钓","篝火晚会","大海冲浪"]
dict['items']=list
json.dump(dict,open('json.json','w',encoding='utf-8'),ensure_ascii=False)
'''

#json.load()  将json文件内容读到内存中
obj=json.load(open('json.json','r',encoding='utf-8'))
print(obj)