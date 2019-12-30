'''
创建带参数和返回值的装饰器
'''
# from functools import wraps
# def decor(f):
#     @wraps(f)    # 解决被装饰函数不能查看信息的bug
#     def inner(a,b):
#         print('*******')
#         d=f(a,b)
#         print('*******')
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