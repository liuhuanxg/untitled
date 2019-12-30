# Python 0715 吕佳

'''
不可变类型的参数：数字、字符串、元组
函数hs(a)内部修改a的值，只是修改了一个副本，不会对a本身造成影响
可变类型的参数：列表、字典、集合
fun(la)将la真正的传过去，修改后fun外部的la也会受影响
'''
# def hs(a):
#     a+=3
#     print('函数内部为a=',a)
# x=10
# hs(x)
# print('函数外部x=',x)

# def hs(a):
#     a.append(3)
#     print(a)
# x=[1,2]
# hs(x)
# print(x)

# def hs(a):
#     a['age']=19
#     print(a)
# x={'name':'张三'}
# hs(x)
# print(x)

# 默认参数如果是可更改类型，程序运行时会有逻辑错误
# 逻辑错误
# def hs(a=[]):
#     a.append(10)
#     print(a)
# hs()
# hs()

# 实参走后对形参没有任何影响，除非再来
# def hs(a=[]):
#     a.append(10)
#     print(a)
# hs()
# b=[9]
# hs(b)
# hs()
# hs(b)

# def hs(a):
#     a=[1,2]    # 这里是重新赋值，不叫修改
# b=[3,4]
# hs(b)
# print(b)

# def hs():
#     b=3
#     print(a)
#     print(b)
# a=6
# hs()

# def hs():
#     a=7
#     print(a)
# a=9
# hs()
# print(a)

# def hs():
#     a=9
#     print(a)
# a=10
# hs()
# print(a)

# def hs():
#     print(a)
# a=10
# hs()

# def hs():
#     global a
#     a+=10
#     print('函数内部：%d'% a)
# a=20
# hs()
# print('函数外部：%d'% a)

# def hs():
#     global a
#     a=10
# hs()
# print(a)

# def hs():
#     global a
#     a=10
# # print(a)
# hs()
# print(a)

# def outside():
#     def inside():
#         print('我是内部')
#     inside()
#     print('我是外部')
# outside()

# def out():
#     a=9
#     def inside():
#         a=98
#         print('我是内部',a)
#     inside()
#     print('我是外部',a)
# out()

# a=9
# def out():
#     def inside():
#         nonlocal a
#         a=98
#         print(a)
#     inside()
#     print(a)
# out()

# a=9
# def out():
#     a=7
#     def inside():
#         nonlocal a
#         a=999
#         print(a)
#     inside()
#     print('---------------',a)
# out()
# print(a)

# a=10
# b=[]
# def x():
#     a=8
#     b.append(9)
#     print(a)
# x()
# print(a)
# print(b)

# b=[]
# def x():
#     a=8
#     b=[9]
#     print(b)
# x()
# print(b)

# a=3
# b=4
# def hs(x):
#     c=5
#     d=6
#     print(locals())
# print(globals())
# hs(6)

'''
local enclosing global built-in
'''
# a=3
# b=30
# c=300
# def out():
#     a=4
#     b=40
#     def inside():
#         a=5
#         print(a)
#         print(b)
#         print(c)
#         print(__name__)
#     inside()
# out()

# x=18
# if x<25:
#     b=20
# print(b)

# a=-1
# b=2
# print(abs(a))
# print(abs(b))

# a=[1,3,4,5,3]
# x=max(a)
# print(x)

# a=[-1,-3,-2,-5,-4]
# b=max(a)
# print(b)

# a=[-1,-3,-2,-5,-4]
# b=max(a,key=abs)
# print(b)

# def hs(x):
#     print('-----')
#     return abs(x)
# a=[-1,-3,-2,-5,-4]
# b=max(a,key=hs)
# print(b)
'''
-----
-----
-----
-----
-----
-5
'''

# lst=[{'name':'Tom','age':19},{'name':'jerry','age':29},{'name':'mary','age':39}]
# def getAge(x):
#     return x['age']
# b=max(lst,key=getAge)
# print(b)

# a=[-1,-3,-2,-5,-4]
# a.sort()
# print(a)
# a.sort(key=abs)
# print(a)

# def hs(x):
#     return x*x
# a=[1,2,3]
# b=map(hs,a)
# print(b)
# print(list(b))

# def gl(a):
#     if a%3==0 or a%7==0:
#         return True
#     else:
#         return False
# a=[1,2,3,4,5,6,7,8,9]
# b=filter(gl,a)
# print(b)
# print(list(b))

# a=[1,2,3]
# b=['a','b','c','d']
# c=zip(a,b)
# print(c)
# for x in c:
#     print(x)

# a=[1,2,3]
# b=['a','b','c','d']
# def hs(x):
#     return {x[0]:x[1]}
# x=map(hs,zip(a,b))
# print(list(x))

# hs=lambda x,y:x+y
# b=hs(2,3)
# print(b)

# func=lambda :3<2
# print(func())

# lst=[{'name':'Tom','age':19},{'name':'jerry','age':29},{'name':'mary','age':39}]
# getAge=lambda x: x['age']
# l=max(lst,key=getAge)
# print(l)

# hs=lambda  x:x*x
# a=[1,2,3]
# b=map(hs,a)
# print(list(b))

# hs=lambda x:True if x%2==0 else False
# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(hs,a)
# print(list(b))

# hs=lambda x:True if x%7==0 or x%3==0 else False
# a=[1,2,3,4,5,6,7,8,9,10]
# b=filter(hs,a)
# print(list(b))

# a=[1,2,3]
# b=['a','b','c']
# hs=lambda x:{x[0]:x[1]}
# x=map(hs,zip(a,b))
# print(list(x))

# i=4
# def hs():
#     print(i+1)
# i=5
# hs()
# i=6
# hs()
# i=7
# hs()

# def hs():
#     x=3
#     def nb(n):
#         return x**n
#     return nb
# b=hs()
# print(b(2))
# print(b(3))

# def hs():
#     x=2
#     def nb(n,x=x):
#         return x**n
#     return nb
# b=hs()
# print(b(3))
# print(b(2,3))

# def hs():
#     a=[]
#     for i in range(3):
#         b=lambda y:y*i
#         a.append(b)
#     return a
# z=hs()
# print(z)
# i=9
# print(z[0](2))
# print(z[1](2))
# print(z[2](2))

# i=6
# def x1(x=i):
#     print(x)
# i=7
# def x2(x=i):
#     print(x)
# x1()
# x2()

# def hs():
#     a=[]
#     for i in range(3):
#         b=lambda y,i=i:y*i
#         a.append(b)
#     return a
# z=hs()
# print(z)
# i=9
# print(z[0](2))
# print(z[1](2))
# print(z[2](2))

# ------------------------------------------------------------------------------
# 作业题
# 不可变数据类型和可变数据类型自加的区别
# 1. 判断gl_num和gl_list的值
# def demo(num,num_list):
#     num+=num
#
#     num_list+=num_list
#
#     print(num)    # 18
#     print(num_list)    # [1,2,3,1,2,3]
#
#     print('函数结束')
# gl_num=9
# gl_list=[1,2,3]
# demo(gl_num,gl_list)
# print(gl_num)    # 9
# print(gl_list)    # [1,2,3,1,2,3]

'''
!!!错了。。。
'''
# 传值和传址问题
# 2.请说出 list1,list2,list3 的值是什么，并且说明为什么
def extendlist(val,lis=[]):
    lis.append(val)
    return lis
list1=extendlist(10)
list2=extendlist(123,[])
list3=extendlist('a')
print(list1)    # [10,'a']
print(list2)    # [123]
print(list3)    # [10,'a']

# 匿名函数
# 3.请说出acts[0](2)的值，并且说明为什么
def makeActions():
    acts=[]
    for i in range(5):
        acts.append(lambda x:i**x)
    return acts
acts=makeActions()
print(acts[0](2))    # 16
print(acts[1](2))    # 16
print(acts[2](2))    # 16
print(acts[3](2))    # 16
print(acts[4](2))    # 16
'''
因为使用了闭包，资源就不会被回收
makeActions()函数执行完，for循环就已经执行过了，这是i=4
在调用acts[i]时的i值就是4
'''