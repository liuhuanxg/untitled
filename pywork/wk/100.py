# 1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and i!=k:
#                 print(i*100+j*10+k)

# 3.一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
假设该数为 x。
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
7、接下来将 i 的所有数字循环计算即可。
'''

# 4.输入某年某月某日，判断这一天是这一年的第几天？
# year=[31,28,31,30,31,30,31,31,30,31,30,31]
# y=int(input('请输入年份：'))
# m=int(input('请输入月份：'))
# d=int(input('请输入日期：'))
# # 判断是否是闰年
# def r():
#     if y%4==0 and y%100!=0 or y%400==0:
#         return True
#     else:
#         return False
# # 判断输入数据是否有效
# def eff():
#     if m>12 or m<1:
#         return False
#     if m in (1,3,5,7,8,10,12):
#         if d>31 or d<1:
#             return False
#     elif m==2:
#         if r():
#             if d>29 or d<1:
#                 return False
#         else:
#             if d>28 or d<1:
#                 return False
#     else:
#         if d>30 or d<1:
#             return False
#     return True
# # 计算
# def count():
#     if eff():    # 有效
#         days=0
#         if r():    #闰年
#             if m>2:
#                 days+=1
#         for i in range(m-1):
#             days+=year[i]
#         for i in range(d):
#             days+=1
#         print('这是{}年的第{}天'.format(y,days))
#     else:
#         print('数据无效')
# count()

# 5.输入三个整数x,y,z，请把这三个数由小到大输出。
# lst=[]
# for i in range(3):
#     x=input('请输入一个整数：')
#     lst.append(x)
# lst.sort()
# for i in range(3):
#     print(lst[i])

# 5.斐波那契数列。
# 递归
# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(1,11):
#     print(fib(i))

# 循环
# def fib(n):
#     i=1
#     a,b=0,1
#     while i<=n:
#         a,b=b,a+b
#         print(a)
#         i+=1
# fib(10)

# 7.将一个列表的数据复制到另一个列表中。
# a=[1,2,3]
# b=a[:]
# print(b)

# 8.输出 9*9 乘法口诀表。
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()

# 9.暂停一秒输出。
# import time
# dic={1:'a',2:'b',3:'c'}
# for k,v in dic.items():
#     print('{}:{}'.format(k,v))
#     time.sleep(1)

# 10.暂停一秒输出，并格式化当前时间。
# import time
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))








