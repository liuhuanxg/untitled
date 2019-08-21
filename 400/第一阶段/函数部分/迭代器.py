'''
可迭代对象：可以直接作用于for循环的对象称为可迭代对象：（Iterable）。
可以用instance（）去判断一个对象是否是（Iterable）对象。

可以直接作用于for的数据类型一般分为两种:
1、集合数据类型，如：list、dict、set、string   可以迭代但不是迭代器
2、是generator，包括生成器和带yield的generator  function
'''
from collections import Iterable#判断是不是可以迭代的
from collections import Iterator#判断是不是迭代器
print(isinstance([],Iterable))    #True
print(isinstance((),Iterable))    #True
print(isinstance({},Iterable))    #True
print(isinstance('',Iterable))    #True
print(isinstance((x for x in range(10)),Iterable))    #True
print(isinstance(1,Iterable))     #False

'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
直到最后抛出一个错误StopIteration表示无法继续返回下一个值。

可以被next（）函数调用并不断返回下一个值的对象称为迭代器（Iterator对象)

可以使用isinstance（）函数判断一个对象是不是Iterator对象

'''
# print(isinstance([],Iterator))
# print(isinstance((),Iterator))
# print(isinstance({},Iterator))
# print(isinstance('',Iterator))
# print(isinstance((x for x in range(10)),Iterator))

# l=(x for x in range(5))   # 迭代器
# print(type(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))



# a=iter([1,2,3,4,5])#转化为迭代器
# print(next(a))
# print(next(a))
# print(isinstance(iter([]),Iterator))
# print(isinstance(iter(()),Iterator))
# print(isinstance(iter({}),Iterator))
# print(isinstance(iter('T'),Iterator))



# endstr='33'
# str=''
# for line in iter(input,endstr):
#     str+=line+'\n'
# print(str)

# def fbnq(n):
#     a,b=0,1
#     count=0
#     while count<n:
#         yield b
#         a,b=b,a+b
#         count+=1
# x=fbnq(5)
# print(next(x))
# print('记号1')
# print(next(x))
# print('记号2')
# print(next(x))
# print(next(x))
# print(next(x))



#斐波那契
'''
def fbnq(n):
    a,b=0,1
    count =1
    c=0
    while count<=n:
        c=a
        a,b=b,a+b
        count+=1
    print(c)
if __name__ == '__main__':
    n=int(input('请输入一个整数：'))
    fbnq(n)
'''


# movie_data = {"宝贝当家": [45, 2, 9, "喜剧片"],
#               "美人鱼": [21, 17, 5, "喜剧片"],
#               "澳门风云3": [54, 9, 11, "喜剧片"],
#               "功夫熊猫3": [39, 0, 31, "喜剧片"],
#               "谍影重重": [5, 2, 57, "动作片"],
#               "叶问3": [3, 2, 65, "动作片"],
#               "伦敦陷落": [2, 3, 55, "动作片"],
#               "我的特工爷爷": [6, 4, 21, "动作片"],
#               "奔爱": [7, 46, 4, "爱情片"],
#               "夜孔雀": [9, 39, 8, "爱情片"],
#               "代理情人": [9, 38, 2, "爱情片"],
#               "新步步惊心": [8, 34, 17, "爱情片"]}
# list=[]
# for key,val in movie_data.items():
#     print(key,val[1])
#     list.append([key,val[1]])
#
# print(list)
# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i][1]<list[j][1]:
#             list[i],list[j]=list[j], list[i]
# print(list)