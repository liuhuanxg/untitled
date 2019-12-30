'''
闭包
要求：
1.闭包函数必须有内嵌函数
2.内嵌函数必须要引用外层函数的变量
3.闭包函数返回内嵌函数的地址（函数名称）
闭包会保留资源，不释放
'''
# def out(b):
#     a=3
#     def inside(x):
#         return a*x+b
#     return inside
# func=out(3)
# print(func(3))

# 判断闭包函数的方法__closure__
# def out(b):
#     a=3
#     def inside(x):
#         return a*x+b
#     print(inside.__closure__)    # 有cell元素，是闭包
#     return inside
# func=out(3)
# print(func(3))

# def out():
#     b=9
#     def inner():
#         print('haha')
#     print(inner.__closure__)    # None--不是闭包
#     return inner
# x=out()
# x()

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
#
# b=[lambda x,i=i:x**i for i in range(3)]
# print(b[0](2))
# print(b[1](2))
# print(b[2](2))