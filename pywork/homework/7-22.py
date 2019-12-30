# Python 0715 吕佳

'''
函数：
def 函数名():
    代码段
组织好的，可重复使用的，用来实现独立功能的代码段
可以提高程序的代码重用率
'''
# def prt():
#     print('1楼、鞋类商品')
#     print('2楼、女性服饰')
#     print('3楼、男装')
#     print('4楼、运动装')
#     print('5楼、婴幼儿用品')
# floor=int(input('请输入楼层：'))
# if floor==1:
#     print('西单大悦城1层欢迎您')
#     prt()
#     print('您现在在1楼')
# elif floor==2:
#     print('西单大悦城2层欢迎您')
#     prt()
#     print('您现在在2楼')
# elif floor==3:
#     print('西单大悦城3层欢迎您')
#     prt()
#     print('您现在在3楼')
# elif floor==4:
#     print('西单大悦城4层欢迎您')
#     prt()
#     print('您现在在4楼')
# elif floor==5:
#     print('西单大悦城5层欢迎您')
#     prt()
#     print('您现在在5楼')

'''
函数：
只在调用的时候执行
函数必须先定义后调用

参数--argument
定义的时候，称为形参，因为没有实际的值
调用时，你给它什么值，它就是什么值
'''
# def qiuhe(a,b):
#     c=a+b
#     print(c)
# qiuhe(2,3)
# qiuhe(5,6)

# 函数调用的本质是函数名对应的内存地址
# def qiuhe(a,b,c):
#     s=a+b+c
#     print(s)
# qiuhe(1,2,3)
# print(qiuhe)
# qh=qiuhe
# print(id(qiuhe))
# print(id(qh))
# qiuhe(1,2,3)

# def hs():
#     print(i+1)
# i=5
# a=hs
# b=hs
# a()    # 6
# i=7
# a()    # 8
# b()    # 8

# def hs(a,b,c):
#     print(a,b,c)
# hs(2,3,c=7)
# hs(a=2,4,5)    # 报错

# 默认函数
# def dengji(name,age,sex='男'):
#     print(name,age,sex)
# dengji('张三',19)
# dengji('李四',20,'男')
# dengji('王五',21,'女')

# def xiaozhu(a=3,b):    # 报错
# # def xiaozhu(b,a=3):
#     print(a,b)
# xiaozhu(1,2)

'''
可变参数
'*'
1.'*'使参数变为了一个元组，所有传递的参数变为元组的元素
2.'*'具有打散序列的功能

'**'
1.'**'使参数变成一个字典，所有传递的参数变为字典的键值对
!!!这里传参要求是键=值的形式
2.'**'有打散字典的功能，实参的key值必须与形参名相同，否则报错
3.'**kwargs'必须放在'*args'后面
'''
# 是函数变成元组
# def kb(*a):
#     print(type(a))
#     for x in a:
#         print(x)
# kb(1)
# kb(1,2,3,4)
# kb()

# def kb(*a):
#     print(a)
# x=(1,2,3)
# kb(*x)
# kb(x)

# 打散序列
# def func(a,b,c):
#     print(a,b,c)
# tup=(1,2,3)
# func(*tup)
# lst=[1,2,3]
# func(*lst)

# def kb(**kwargs):
#     print(kwargs,type(kwargs))
# kb(name='张三',age=18)
# kb(name='张三',age=18,sex='男')
# kb()

# def kb(name,age):
#     print(name,age)
# a={'name':'张三','age':18}
# kb(**a)

# def kb(*a,**b):
#     print(a,b)
# a={'name':'张三','age':19}
# kb(1,2,3,**a)
# kb(1,2,3,*a)

# def kb(a,*b,c=9,**d):
#     print('a=', a)
#     print('b=', b)
#     print('c=', c)
#     print('d=', d)
# # kb(1,2,3,4,5)
# kb(1,2,3,name='张三')

# def hs1(x,y):
#     print(x*y)
# def hs2(a,b,c):
#     hs1(a,b)
#     print(c)
# hs2(2,3,4)

# def jo(a):
#     if a%2==0:
#         print(a,'是偶数')
#     else:
#         print(a,'是奇数')
# num=int(input('请输入一个数：'))
# jo(num)

# def qiuhe(a,b):
#     c=a+b
#     return c
# x=qiuhe(1,2)
# print(x)
# y=qiuhe(10,20)
# print(y)

# a=[1,2,30]
# x=a.remove(30)
# print(x)

# def hs(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     return c,d,e
# x=hs(5,6)
# print(x)
# x,y,z=hs(5,6)
# print(x,y,z)

# def hanshu(a,b):
#     return
#     c=a+b
#     d=a-b
#     return c,d
# x=hanshu(5,6)
# print(x)

# def hs():
#     i=0
#     while i<5:
#         if i==2:
#             return
#         i+=1
# x=hs()
# print(x)

# def total(price,num):
#     return price*num
# def pd():
#     t=total(price,num)
#     if t>300:
#         return t*0.8
#     else:
#         return int(t)-int(t%10)
# price=float(input('请输入西红柿单价：'))
# num=float(input('请输入购买数量：'))
# print('最终价格为：',pd())

# def jiecheng(n):
#     if n==1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# x=jiecheng(6)
# print(x)

# def tuzi(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return tuzi(n-1)+tuzi(n-2)
# n=int(input('请输入月份：'))
# for i in range(1,n+1):
#     print('第',i,'个月的兔子数为：',tuzi(i))

# def tuzi(n):
#     a,b=1,1
#     for i in range(1,n+1):
#         if i==1 or i==2:
#             print(a,end='\t')
#         else:
#             a,b=b,a+b
#             print(b,end='\t')
# n=int(input('请输入月份：'))
# tuzi(n)

# def p_n(n):
#     print(n)
#     if n==1:
#         return
#     p_n(n-1)
#     print('-->')
# p_n(4)

# def zbcz(a,start,end,key):
#     if start>end:
#         return -1
#     middle=(start+end)//2
#     if key<a[middle]:
#         return zbcz(a,start,middle-1,key)
#     elif key>a[middle]:
#         return zbcz(a,middle+1,end,key)
#     else:
#         return middle
# a=[1,2,3,4,5,6,7,8,9,10]
# k=int(input('请输入想要查找的数：'))
# x=zbcz(a,0,len(a)-1,k)
# if x>=0:
#     print(k,'的位置为：',x)
# else:
#     print('该序列中没有',k)

# def zbcz(a,start,end,k):
#     while start<=end:
#         middle=(start+end)//2
#         if k>a[middle]:
#             start=middle+1
#         elif k<a[middle]:
#             end=middle-1
#         else:
#             return middle
#     return -1
# a=[1,2,3,4,5,6,7,8,9,10]
# k=int(input('请输入想要查找的数：'))
# x=zbcz(a,0,len(a)-1,k)
# if x>=0:
#     print(k,'的位置为：',x)
# else:
#     print('该序列中没有',k)

# def hs1(x,y):
#     print(x*y)
# def hs2(a,b,c):
#     hs1(a,b)
#     print(c)
# hs2(2,3,4)

# def jo(a):
#     if a%2==0:
#         print(a,'是偶数')
#     else:
#         print(a,'是奇数')
# num=int(input('请输入一个数：'))
# jo(num)

# def hanshu(a,b):
#     return
#     c=a+b
#     return c,d
# x=hanshu(5,6)
# print(x)

# def hs():
#     i=0
#     while i<5:
#         if i==2:
#             return
#         i+=1
# x=hs()
# print(x)

# def total(price,num):
#     return price*num
# def pd():
#     t=total(price,num)
#     if t>300:
#         return t*0.8
#     else:
#         return int(t)-int(t%10)
# price=float(input('请输入西红柿单价：'))
# num=float(input('请输入购买数量：'))
# print('最终价格为：',pd())

# def jiecheng(n):
#     if n==1:
#         return 1
#     else:
#         return n*jiecheng(n-1)
# x=jiecheng(6)
# print(x)

# def tuzi(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return tuzi(n-1)+tuzi(n-2)
# n=int(input('请输入月份：'))
# for i in range(1,n+1):
#     print('第',i,'个月的兔子数为：',tuzi(i))

# def tuzi(n):
#     a,b=1,1
#     for i in range(1,n+1):
#         if i==1 or i==2:
#             print(1,end='\t')
#         else:
#             a,b=b,a+b
#             print(b,end='\t')
# n=int(input('请输入月份：'))
# tuzi(n)

# def p_n(n):
#     print(n)
#     if n==1:
#         return
#     p_n(n-1)
#     print('-->')
# p_n(4)

# def zbcz(a,start,end,key):
#     if start>end:
#         return -1
#     middle=(start+end)//2
#     if key<a[middle]:
#         return zbcz(a,start,middle-1,key)
#     elif key>a[middle]:
#         return zbcz(a,middle+1,end,key)
#     else:
#         return middle
# a=[1,2,3,4,5,6,7,8,9,10]
# k=int(input('请输入想要查询的数：'))
# x=zbcz(a,0,len(a)-1,k)
# if x>=0:
#     print(k,'的位置为：',x)
# else:
#     print('该序列中没有',k)

# def zbcz(a,start,end,k):
#     while start<=end:
#         middle=(start+end)//2
#         if k > a[middle]:
#             start=middle+1
#         elif k<a[middle]:
#             end=middle-1
#         else:
#             return middle
#     return -1
# a=[1,2,3,4,5,6,7,8,9,10]
# k=int(input('请输入想要查找的数：'))
# x=zbcz(a,0,len(a)-1,k)
# if x>=0:
#     print(k,'的位置为：',x)
# else:
#     print('该序列中没有',k)

# ------------------------------------------------------------------------------
# 作业题
# 1、写一个函数实现斐波那契数列(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377......)
# 要求：接收一个参数，返回一个存着等量值的列表
# lst=[]
# def func(num):
#     a=1
#     b=1
#     for i in range(1,num+1):
#         if i==1 or i==2:
#             lst.append(1)
#         else:
#             a,b=b,a+b
#             lst.append(b)
# func(6)
# print(lst)
# 2.计算任意多个数字的和
# 需求
# (1).定义一个函数 sum_numbers，可以接收的 任意多个整数
# (2).功能要求：将传递的 所有数字累加 并且返回累加结果
# def sum_numbers(*args):
#     s = 0
#     for i in args:
#         s+=i
#     print(s)
# sum_numbers(1,2,3)
# sum_numbers(1,8,10,11)
# 3.使用递归，计算 1 + 2 + ... num 的结果
# def sum(num):
#     if num==1:
#         return 1
#     else:
#         return num+sum(num-1)
# num=int(input('请输入想要求和的数是从1到：'))
# print(sum(num))