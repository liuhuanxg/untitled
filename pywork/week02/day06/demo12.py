'''
过滤
filter()--过滤序列
过滤掉不符合条件的元素，返回由符合条件元素组成的可迭代对象
第一个参数是一个函数名，第二个参数是序列
    返回的是True或False
最后将返回True的元素放入新的可迭代对象
'''
def gl(a):
    if a%3==0 or a%7==0:
        return True
    else:
        return False
a=[1,2,3,4,5,6,7,8,9]
b=filter(gl,a)
print(b)    # <filter object at 0x0000000002662860>
print(list(b))    # [3, 6, 7, 9]