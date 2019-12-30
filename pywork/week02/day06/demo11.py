'''
映射
map()--第一个参数是一个函数名，第二个参数是可迭代的内容
        返回的是加工过的值
函数会依次作用在迭代内容的每一个元素上进行计算，然后返回一个新的可迭代对象
'''
def hs(x):
    return x*x
a=[1,2,3]
b=map(hs,a)
print(b)    # <map object at 0x0000000002142860>
# for x in b:
#     print(x)
b=list(b)
print(b)