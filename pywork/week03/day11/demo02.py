'''
__call__()方法
可以让类的实例具有类似于函数的行为，进一步模糊了函数和对象之间的概念。
对象后面加括号，就像函数调用一样触发执行。对象()或类()()
'''
# class A():
#     def __init__(self,num):
#         self.num=num
#     def __call__(self,n):
#         return self.num*n
# a=A(7)
# print(a(9))
# print(A(3)(7))

# class Fib():
#     def __init__(self):
#         pass
#     def __call__(self,month):
#         lst=[]
#         a,b=1,1
#         n=1
#         while n<=month:
#             lst.append(a)
#             a,b=b,a+b
#             n+=1
#         return lst
# f=Fib()
# for i in range(1,10):
#     print(f(i))

# class Fib():
#     def __init__(self):
#         pass
#     def __call__(self,month):
#         a,b=0,1
#         n=1
#         while n<=month:
#             a,b=b,a+b
#             n+=1
#         return a
# f=Fib()
# m=int(input('请输入：'))
# print(f(m))