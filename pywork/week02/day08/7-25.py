# Python0715 吕佳

'''
列表推导式
'''
# a=[1,2,3,4,5,6]
# b=[i*i for i in a]
# print(b)

# a=[1,2,3,4,5,6]
# x=map(lambda c:c*c,a)
# print(list(x))

# a=[1,2,3,4,5,6]
# def qiupf(x):
#     return x*x
# b=[qiupf(i) for i in a]
# print(b)

# a=[1,2,3,4,5,6]
# b=[i for i in a if i%2==1]
# print(b)

# a=[1,2,3,4,5,6]
# b=[i**2 for i in a if i%2==0 if i>2]
# print(b)
# b=[i**2 for i in a if i%2==0 and i>2]
# print(b)

# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         print(a[i][j],end=' ')
#         j+=1
#     print()
#     i+=1

# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# b=[y for x in a for y in x]
# print(b)

# 输出1 4 7
# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# b=[a[i][0] for i in range(len(a))]
# print(b)

# 输出1 5 9
# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# b=[a[i][i] for i in range(len(a))]
# print(b)

# 输出3 5 7
# a=[[1,2,3,0],[4,5,6],[7,8,9]]
# b=[a[i][len(a)-1-i] for i in range(len(a))]
# print(b)

# 生成a=[[1,2,3],[4,5,6],[7,8,9]]
# a=[]
# for i in range(3):
#     b=[]
#     for j in range(3):
#         x=3*i+1+j
#         b.append(x)
#     a.append(b)
# print(a)

# a=[[3*i+1+j for j in range(3)]for i in range(3)]
# print(a)

# a=[lambda x:x*i for i in range(3)]
# print(a[0](2))
# print(a[1](2))
# print(a[2](2))

'''
字典推导式
'''
# a={'a':'b',1:2}
# b={v:k for k,v in a.items()}
# print(b)

# a={k:v for k,v in zip('abc','123')}
# print(a)

# a={'a':1,'A':3,'b':4,'B':9,'c':10,'d':99}
# x=['a','A','B','b','c']
# b={k.lower():a.get(k.lower(),0)+a.get(k.upper(),0)for k in a.keys() if k in x}
# print(b)

'''
集合推导式
'''
# a=[1,2,3,4,1,2,3,4]
# b={i*i for i in a}
# print(b)

'''
生成器
'''
# a=[1,2,3,4]
# b=(i*i for i in a)
# print(b)
# print(tuple(b))

'''
模块
一个包括了python代码的文件就是一个模块
作用：
1.方便维护与管理
2.增加代码的重用率
模块只有被第一次导入的时候执行，多次导入没有用
'''
# import demo04 as ha
# print(ha.sum(2,3))

'''
模块导入：
1.模块导入会将导入的文件执行一遍
2.导入的名称就是我们定义的脚本或包的名称
3.导入的过程：
在指定范围内搜索指定名称的python脚本或者包，将其运行，获取其中的方法
'''
# import demo04
# import demo04

'''
模块导入的方式：
1.import 模块名
2.import 模块名 as 别名
3.import 模块名1，模块名2，...--一行导入多个模块
'''
# import time
# print(time.time())
#
# import time as t
# print(t.time())
#
# import time,sys,os
# print(time.time())
# print(sys.path)
# print(os.getcwd())

'''
4.from...import...--局部导入
5.from...import...as 别名
6.from...import 功能1，功能2,...
7.from...import *--导入所有
'''
# from demo04 import sum,qiuji
# print(sum(2,3))
# print(qiuji(2,3))

# from demo04 import sum as s
# print(s(2,3))

# from model import * 不能导入_开头的变量
# from demo04 import *
# print(sum(2,3))
# print(qiuji(2,3))
# print(cha(5,2))
# print(x)
# # print(_y)    # 报错

# 就近原理
# x=9
# print(x)    # 9
# from demo04 import *
# print(x)    # 100

# from demo04 import *
# x=9
# print(x)    # 9

'''
用from model import *时
__all__=[变量1，变量2,...]只能导入__all__列表中的名字
_开头的名字也可以用from model import *导入
'''
# import demo09
# print(demo09.hs1(1,3))
# print(demo09.hs2(1,3))
# print(demo09._hs3(1,3))

# from demo09 import *
# print(hs1(1,3))
# print(hs2(1,3))
# print(_hs3(1,3))

'''
模块搜索路径
搜索顺序：
1.当前目录
2.搜索在shell变量pythonPATH下的每个目录，由sys模块的sys.path方法来规定
'''
# import sys
# print(sys.path)
# sys.path.append('E:\\pywork\\day01')
# print(sys.path)
# import ex
# print(ex.sum(1,2))

# import demo12

'''
random模块
random()--产生大于0且小于1之间的小数
uniform(a,b)--产生指定范围内的随机小数
randint(a,b)--产生范围内的随机整数，包含头和尾
randrange(s,e,[step])--产生范围内的随机整数，左闭右开
choice(lst)--随机返回序列中的一个数据
shuffle()--打乱列表顺序，直接修改原列表
'''
import random
# print(random.random())
# print(random.uniform(2,3))

# a=[random.randint(1,10) for i in range(10)]
# print(a)

# a=random.randrange(1,13,2)
# print(a)
# a=[random.randrange(1,10,3)for i in range(10)]
# print(a)

# a=[10,20,30,40]
# b=random.choice(a)
# print(b)

# a=[10,20,30,40]
# b=random.shuffle(a)
# print(b)

# 生成随机验证码
# import random
# def verify_code():
#     code=''
#     for i in range(4):
#         sz=random.randint(0,9)
#         xzm=chr(random.randint(97,122))
#         dzm=chr(random.randint(65,90))
#         c=random.choice([sz,xzm,dzm])
#         code=code+str(c)
#     return code
# print(verify_code())

import sys
# print(sys.version)

# argv--接受命令行下的参数
# ret=sys.argv
# path=sys.argv[0]
# name=sys.argv[1]
# pwd=sys.argv[2]
# if name=='zs' and pwd=='123':
#     print('登录成功')
# else:
#     print('失败')

import time
# print(time.time())
# time.sleep(3)
# print(time.time())

# 获取时间元组，可接受时间戳参数
# ret=time.localtime()
# print(ret)
# print(time.localtime(time.time()-3600))

# 时间字符串格式化
# 时间元组转换为字符串
# a=time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
# print(a,type(a))
#
# # 字符串转换为时间元组
# b=time.strptime(a,'%Y-%m-%d %H-%M-%S')
# print(b)
#
# # 时间元组转换为时间戳
# x=time.mktime(b)
# print(x)
#
# # 时间戳转换为时间元组
# y=time.localtime(x)
# print(y)

# UTC--国际协调时间，比北京时间少8小时
# s=time.gmtime()
# print(s)
# ------------------------------------------------------------------------------
# 作业题
# 列表推导式

# 1.创建一个函数，输入一个大于1的整数，返回一个列表，
# 包含所有能够整除该整数的因子（不包含1和它本身），并且从小到大排序。
# 如果这个数是素数，则返回“(integer) is prime”。
# 函数
# def div1(data):
#     a=[]
#     for i in range(2,data):
#         if data%i==0:
#             a.append(i)
#     if len(a):
#         return a
#     else:
#         return '%d is prime'%data
# print(div1(12))
# print(div1(25))
# print(div1(13))

# 推导式
# def div2(data):
#     a=[i for i in range(2,data)if data%i==0]
#     return a if len(a) else '%d is prime'%data
# print(div2(12))
# print(div2(25))
# print(div2(13))

# 2.使用列表推导式将一个二维列表转换成一个一维列表。
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 转换成:lst2=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# lst1=[y for x in lst for y in x]
# print(lst1)

# 3.现在有一列表lst = [[1,2,3],[4,5,6],[7,8,9]]
# 要求使用列表推导式取出 1、4、7  和 1、5、9 元素，思考如何取出
# lst = [[1,2,3],[4,5,6],[7,8,9]]
# a=[lst[i][0] for i in range(3)]
# print(a)
# a=[lst[i][i] for i in range(3)]
# print(a)

# 列表推导式+ 匿名函数 + for循环
# data=range(10)
# funcs=[lambda x:i*x for i in data]
# for func in funcs:
#     print(func(2))