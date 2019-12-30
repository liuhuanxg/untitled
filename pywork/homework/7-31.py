# Python 0715 吕佳
'''
迭代器
只要含有__iter__()的都是可迭代的
'''
# b='abcdef'
# for x,y in enumerate(b):
#     print(x,y)
# print(dir([]))

# 查看共有方法
# print(set(dir([]))&set(dir(''))&set(dir({}))&set(dir(range(2))))

# 说明int类型不可迭代
# print('__iter__'in dir(int))

'''
迭代器中的方法比列表中的多了{'__setstate__', '__length_hint__', '__next__'}
__length_hint__--获取元素的个数
__setstate__--决定取值的位置
__next__--获取元素
'''
# a=set(dir([].__iter__()))
# b=set(dir([]))
# print(a-b)

# __iter__()作用：返回一个迭代器
# print([].__iter__())

# k=[1,2,3]
# d=k.__iter__()
# print(d.__next__())
# print(d.__next__())
# print(next(d))

'''
迭代器的应用场景
'''
# 1.数据类型转换
# str1='hello'
# lst1=list(str1)
# print(lst1)
# tuple1=('a','b','c')
# lst2=list(tuple1)
# print(lst2)

# 2.斐波那契序列
# class Fib():
#     def __init__(self,num):
#         self.num=num
#         self.a=1
#         self.b=1
#         self.current=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current<=self.num:
#             print(self.a)
#             self.a,self.b=self.b,self.a+self.b
#             self.current+=1
#         else:
#             raise StopIteration
# for x in Fib(10):
#     pass

'''
生成器
yield起到了return的功能，但不会结束函数。保留当前函数的状态，等到下次进入继续使用。
'''
# def shengchan(n):
#     i=1
#     while i<n:
#         yield i
#         i+=1
# x=shengchan(5)
# print(x)
# for y in x:
#     print(y)

# def dee():
#     yield 1
#     yield 2
#     yield 3
# x=dee()
# print(x.__next__())
# print(next(x))
# print(x.__next__())

'''
send()
获取下一个值的效果和next()基本一致，只是在获取下一个值的时候，给上一个yield的位置传递一个数据。
'''
# def g():
#     print('a')
#     x=yield 10
#     print('接收到数据',x)
#     yield x+5
# x=g()
# print(next(x))
# b=x.send(999)
# print(b)

'''
应用：
计算平均值，送n个，算n个
'''
# def g():
#     count=1
#     get_num=0
#     avg=0
#     total=0
#     while True:
#         get_num=yield avg
#         total=total+get_num
#         avg=total/count
#         count+=1
# x=g()
# print(next(x))
# print(x.send(10))
# print(x.send(20))
# print(x.send(30))

# def fib(n):
#     a,b=1,1
#     i=1
#     while i<=n:
#         yield a
#         a,b=b,a+b
#         i+=1
# for x in fib(10):
#     print(x)

# 使用for循环取出生成器中所有的值
# def gen1():
#     for c in 'AB':
#         yield c
#     for i in range(3):
#         yield i
# for x in gen1():
#     print(x)

'''
yield from
'''
# def g():
#     yield from 'AB'
#     yield from range(5)
# for x in g():
#     print(x)

'''
生成器表达式
'''
# b=(i for i in range(5))
# print(b)
# for x in b:
#     print(x)

# a=('鸡蛋{}个'.format(i+1)for i in range(10))
# print(a)
# next会记录状态
# print(next(a))
# print(a.__next__())
# print(list(a))

'''
闭包
要求：
1.闭包函数必须有内嵌函数
2.内嵌函数必须要引用外层函数的变量
3.闭包函数返回内嵌函数的地址（函数名称）
闭包会保留资源，不释放
'''
# 判断闭包函数的方法__closure__()
# def out(b):
#     a=3
#     def inside(x):
#         return x*a+b
#     print(inside.__closure__)
#     return inside
# func=out(3)
# print(func(3))

# def out():
#     b=9
#     def inner():
#         print('haha')
#     print(inner.__closure__)
#     return inner
# func=out()
# func()

# def func():
#     x=4
#     lst=[]
#     for i in range(3):
#         action=lambda x,i=i:x**i
#         lst.append(action)
#     return lst
# b=func()
# print(b[0](2))
# print(b[1](2))
# print(b[2](2))

# b=[lambda x,i=i:x**i for i in range(3)]
# print(b[0](2))
# print(b[1](2))
# print(b[2](2))

'''
装饰器的本质：一个闭包函数
作用：在不修改原函数及其调用方式的情况下对原函数功能进行拓展
'''
# import time
# def decor(f):
#     def inner():
#         t = time.time()
#         f()
#         t2 = time.time()
#         print('运行时间为{}'.format(t2 - t))
#     return inner
# @decor
# def func():
#     s=0
#     for i in range(10000000):
#         s+=1
#     print(s)
# func()

# def decor(f):
#     def inner():
#         print('****')
#         f()
#         print('****')
#     return inner
# def decor2(f):
#     def inner():
#         print('####')
#         f()
#         print('####')
#     return inner
# @decor
# @decor2
# def func():
#     print('欢迎')
# @decor
# def func2():
#     print('走好')
# func()
# print()
# func2()

'''
创建带参数和返回值的装饰器
'''
# from functools import wraps
# def decor(f):
#     @wraps(f)
#     def inner(a,b):
#         print('******')
#         d=f(a,b)
#         print('******')
#         return d
#     return inner
# @decor
# def func(a,b):
#     '''
#     :param a:
#     :param b:
#     :return:
#     '''
#     c=a+b
#     return c
# print(func(2,3))
# print(func.__doc__)

'''
@property装饰器--把一个方法的调用方式变为属性调用方式（将一个方法当成一个属性使用）。只能在面向对象中使用。
只能修饰不带参数的方法。
@age.setter--是@property装饰器的副产品，用来修饰setter方法。
'''
# class A():
#     def __init__(self,name):
#         self.name=name
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,age):
#         if age<0 or age>100:
#             print('错误')
#             self.__age=-1
#         else:
#             self.__age=age
# a=A('张三')
# a.age=39
# print(a.age)
# a.age=400
# print(a.age)

# class A():
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name=name
# a=A('张三')
# print(a.name)
# a.name='李四'
# print(a.name)

# from math import pi
# class Circle():
#     def __init__(self,r):
#         self.__r=r
#     @property
#     def c(self):
#         return 2*pi*self.__r
#     @property
#     def area(self):
#         return pi*self.__r**2
# y=Circle(3)
# print(y.c)
# print(y.area)

# class Person():
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#     @property
#     def bmi(self):
#         return self.weight/(self.height**2)
# p=Person('吕佳',48,1.63)
# print(p.bmi)

# --------------------------------------------------------
# 作业题
# 迭代器练习
# 获取素数
# class PrimeNumbers():
#     def __init__(self,start,end):
#         self.start=start
#         self.end=end
#     def isPrimeNumber(self,k):
#         if k<2:
#             return False
#         for i in range(2,k):
#             if k%i==0:
#                 return False
#         return True
#     def __iter__(self):
#         for k in range(self.start,self.end+1):
#             if self.isPrimeNumber(k):
#                 yield k
# for x in PrimeNumbers(1,10):
#     print(x)

# 装饰器练习
"""
（一）需求：打印菱形
1、空格、*号组成的菱形
2、输入菱形上半部分的行数即可打印
3、支持循环输入
"""
# while True:
#     num_str=input('请输入菱形上半部分的正三角的行数：')
#     if num_str.isdigit():
#         n=int(num_str)
#         for i in range(1,n+1):
#             for j in range(1,n-i+1):
#                 print(' ',end='')
#             for j in range(1,2*i):
#                 print('*',end='')
#             print()
#         for i in range(1,n):
#             for j in range(1,i+1):
#                 print(' ',end='')
#             for j in range(1,2*(n-i)):
#                 print('*',end='')
#             print()
#     else:
#         print('输入错误，请重新输入')

# def forever(fun):
#     def inner():
#         while True:
#             n = input("请输入菱形上部的正三角的行数：")
#             if n == "q" or n == "exit":
#                 print("程序已退出！")
#                 break
#             fun(n)
#     return inner
# def verify_number(fun):
#     def inner(n):
#         if isinstance(n,int) or n.isdigit():
#             n=int(n)
#             fun(n)
#         else:
#             print('错误，请重新输入！')
#     return inner
# @forever
# @verify_number
# def prt(n):
#     for i in range(1,n+1):
#         for j in range(1,n-i+1):
#             print(' ',end='')
#         for j in range(1,2*i):
#             print('*',end='')
#         print()
#     for i in range(1,n):
#         for j in range(1,i+1):
#             print(' ',end='')
#         for j in range(1,2*(n-i)):
#             print('*',end='')
#         print()
# prt()