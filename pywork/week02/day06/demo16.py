'''
凡是内部嵌套函数用了外部资源时形成了闭包
资源就不会被回收，在函数运行完之后还存储在内存中
'''
# def hs():
#     x=3
#     def nb(n):
#         return x**n
#     return nb
# b=hs()    # b=nb
# print(b(2))    # 9
# print(b(3))    # 27

# def hs():
#     x=3
#     nb=lambda n:x**n
#     return nb
# b=hs()
# print(b(2))    # 9
# print(b(3))    # 27

# def func():
#     x=2
#     def nb(n,x=x):
#         return x**n
#     return nb
# b=func()
# print(b(3))    # 8
# print(b(2,3))    # 9

# def func():
#     x=2
#     return lambda n,x:x**n
# b=func()
# print(b(3,2))
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
# print(z[0](2))    # 4
# print(z[1](2))    # 4
# print(z[2](2))    # 4

'''
加载函数时，没有调用，函数内的语句不会执行
但因为已经加载，所以默认参数已经赋值了
'''
i=6
def x1(x=i):
    print(x)
i=7
def x2(x=i):
    print(x)
x1()
x2()

# def hs():
#     a=[]
#     for i in range(3):
#         b=lambda y,i=i:y*i
#         a.append(b)
#     return a
# z=hs()
# print(z)
# i=9
# print(z[0](2))    # 0
# print(z[1](2))    # 2
# print(z[2](2))    # 4