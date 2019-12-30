'''
add()--添加，重复不操作
'''
# a={1,2,3,3,3,3,3}
# print(a)
# a.add(9)
# print(a)
# a.add(9)
# print(a)

'''
set()
'''
# a=[1,2,3]
# b=set(a)
# print(b)    # 转换为集合 {1, 2, 3}
# a='1234'
# b=set(a)
# print(b)    # {'2', '1', '4', '3'}，顺序每次执行都可变
# b={'name':'张三','age':19}
# a=set(b)
# print(a)    # {'age', 'name'},只有键没有值

# 顺序遍历
# a={1,2,3,4}
# for x in a:
#     print(x)

'''
update()--添加，不重
'''
a={1,2,3,4}
a.update([1,2,5,6])
print(a)    # {1, 2, 3, 4, 5, 6}
a={1,2,3,4}
a.update({1,2,5,6})
print(a)
a={1,2,3,4}
a.update('a')
print(a)
a={1,2,3,4}
a.update({'name':'tom'})
print(a)
a={1,2,3,4}
a.update((1,2,5,6))
print(a)