'''
装饰器的本质：一个闭包函数
作用：在不修改原函数及其调用方式的情况下对原函数功能进行拓展
'''
# import time
# def decor(f):
#     def inner():
#         t=time.time()
#         f()
#         t2=time.time()
#         print('运行时间：{}'.format(t2-t))
#     return inner
# @decor
# def func():
#     s=0
#     for i in range(1000000):
#         s+=1
#     print(s)
# func()

def decor(f):
    def inner():
        print('****')
        f()
        print('****')
    return inner
def decor2(f):
    def inner():
        print('####')
        f()
        print('####')
    return inner

@decor
@decor2
def f1():
    print('欢迎')

@decor
def f2():
    print('走好')

f1()
print()
f2()