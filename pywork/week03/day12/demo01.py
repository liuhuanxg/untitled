'''
迭代器
只要含有__iter__()的都是可迭代的。
'''
# b='abcdef'
# for x,y in enumerate(b):
#     print(x,y)
# print(dir([]))
# 查看共有方法
# print(set(dir([]))&set(dir(''))&set(dir({}))&set(dir(range(2))))
# 说明int类型不可迭代
# print('__iter__'in dir(int))    # False

'''
{'__setstate__', '__length_hint__', '__next__'}
__length_hint__--获取元素的个数
__setstate__--决定取值的位置
__next__--获取元素
'''
# a=set(dir([].__iter__()))
# b=set(dir([]))
# print(a-b)

# k=[1,2,3]
# d=k.__iter__()
# print(d.__next__())
# print(d.__next__())
# print(d.__next__())

# __iter__()，作用：返回一个迭代器
# print([].__iter__())