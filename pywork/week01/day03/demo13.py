# 强制类型转换  tuple--元组  list--列表
# a=[1,2,3]
# b=tuple(a)
# print(type(b))
# c=list(b)
# print(type(c))

# 元组中','很重要
a=(1)
print(type(a))
a=(1,)
print(type(a))
a=1,2
print(a,type(a))
a=[1]
print(type(a))

# index()--查找参数第一次出现的索引值
a=(1,2,3,4)
print(a.index(4))
# print(a.index(4,0,3))     #报错  后两个参数为查找的范围，同样左闭右开
