'''
zip()--接收任意多个可迭代对象作为参数
将对象中对应元素，打包成一个元组，然后返回一个可迭代的zip对象
若长度不同，以最短的为准
'''
# a=[1,2,3]
# b=['a','b','c','d']
# c=zip(a,b)
# print(c)
# for x in c:
#     print(x)
'''
<zip object at 0x0000000002696D88>
(1, 'a')
(2, 'b')
(3, 'c')
'''

# a=[1,2,3]
# b=['a','b','c']
# def hs(x):
#     return {x[0]:x[1]}
# x=map(hs,zip(a,b))
# print(list(x))    # [{1: 'a'}, {2: 'b'}, {3: 'c'}]