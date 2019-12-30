# 字典--键值对 -- 无序，可修改

'''
字典的key必须是不可修改的类型
'''
#添加
'''
不存在，添加
存在，覆盖
'''
a={'name':'张三','age':19,'sex':'男'}
print(a)
print(a['name'])
a['score']=99
print(a)
a['age']=18
print(a)

'''
setdefault()
存在，不操作
不存在，添加
'''
a={'name':'张三','age':19,'sex':'男'}
a.setdefault('age',20)
print(a)
a.setdefault('score',90)
print(a)

