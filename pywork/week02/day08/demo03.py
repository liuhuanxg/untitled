'''
集合推导式
'''
# a=[1,2,3,4,1,2,3,4]
# b={i*i for i in a}
# print(b)

'''
生成器
'''
a=[1,2,3,4]
b=(i*i for i in a)
print(b)
# for x in b:
#     print(x)