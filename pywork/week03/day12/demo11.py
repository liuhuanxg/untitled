# def myabs(a):
#     print('我是',a)
#     return abs(a)
# a=[1,3,-2,-5,-4]
# b=max(a,key=myabs)
# print(b)

'''
深浅拷贝
'''
import copy
# a=[1,2,3,[4,5]]
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# a.append(999)
# a[3].append(66)
# print(a)
# print(b)
# print(c)
# print(d)

# a=[1,2,(3,4,[5])]
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# x=5
# print(id(a[2][2][0]))
# print(id(x))

# def fib(month):
#     if month==1 or month==2:
#         return 1
#     else:
#         return fib(month-1)+fib(month-2)
# for i in range(1,101):
#     print('第{}个月的兔子数是{}'.format(i,fib(i)))

# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[a[i][0] for i in range(len(a))]
# print(b)
# c=[a[i][i] for i in range(len(a))]
# print(c)

# import time
# a=[1,2,3,4,5,6]
# while True:
#     t=a[0]
#     i=0
#     while i<len(a)-1:
#         a[i]=a[i+1]
#         i+=1
#     a[i]=t
#     print(a)
#     time.sleep(1)

# a=input('请输入母串：')
# b=input('请输入子串：')
# count=0
# i=0
# while i<len(a)-len(b):
#     j=0
#     while j<len(b):
#         if a[i+j]!=b[j]:
#             break
#         j+=1
#     else:
#         count+=1
#         print('位置{}是第{}次找到子串{}'.format(i,count,b))
#     i+=1