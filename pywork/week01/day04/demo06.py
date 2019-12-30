# 查找
'''
keys()--所有key，列表
'''
# a={'name':'张三','age':19,'sex':'男'}
# print(a.keys())    # dict_keys(['name', 'age', 'sex'])
# for i in a.keys():
#     print(i)

'''
values()--所有value，列表
'''
# a={'name':'张三','age':19,'sex':'男'}
# print(a.values())
# for v in a.values():
#     print(v)

'''
items()--所有键值对,元组
'''
a={'name':'张三','age':19,'sex':'男'}
print(a.items())
for kv in a.items():
    print(kv)
for k,v in a.items():
    print(k,v)

'''
len()--返回键值对个数
'''
# a={'name':'张三','age':19,'sex':'男'}
# print(len(a))


'''
get()--以键取值，若指定键不存在，默认返回None，可指定返回值
'''
# info={'name':'张三','age':19,'sex':'男'}
# name=info.get('name')
# print(name)
# a=info.get('a')
# print(a)
# a=info.get('a','不存在')
# print(a)