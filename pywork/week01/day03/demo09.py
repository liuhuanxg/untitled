# a=[1,2,3]
# b=a
# a.append(4)
# print(a,b)
# print(id(a),id(b))
# print(a is b)     #True

'''
is和==的区别：
is判断的是a对象是否就是b对象，是通过id来判断的
==判断的是a对象的值是否和b对象的值相等，是通过value来判断的
'''

a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)

a=3
b=a
a=5
print(a,b)

a='abc'
b='abc'
print(id(a))
print(id(b))