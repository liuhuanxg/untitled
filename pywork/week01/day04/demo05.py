# 删除

'''
pop()--弹出指定键对应的值
不同于列表中的pop()，必须有参数
返回值为value
'''
# a={'name':'张三','age':19,'sex':'男'}
# b=a.pop('name')
# print(b)
# print(a)

'''
popitem()--随机弹出一个键值元组，随机是因为字典无序
返回值为一个键值对元组
'''
# a={'name':'张三','age':19,'sex':'男'}
# b=a.popitem()
# print(b)
# print(a)

'''
清空字典
'''
# a={'name':'张三','age':19,'sex':'男'}
# a.clear()
# print(a)

'''
del--可删除字典中的一个键值对，也可删除整个字典
'''
a={'name':'张三','age':19,'sex':'男'}
del a['name']
print(a)
del a
print(a)    # 报错 字典a不存在