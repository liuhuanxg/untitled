# 静态方法、类方法、实例方法
# class A():
#     count=0
#     def __init__(self,num):
#         self.num=num
#         A.count+=1
#     def f1(self):
#         print(self.num)
#     @staticmethod
#     def f2():
#         print('我跟类和对象都没有关系')
#     @classmethod
#     def f3(cls):
#         print(cls.count)
# A.f3()
# x=A(5)
# x.f1()
# A.f3()
# x.f2()
# A.f2()

# 装饰器
# def timefun(f):
#     def inner(a,b):
#         print(a+b)
#         ret=f()
#         print('--inner--')
#         return ret
#     return inner
# @timefun
# def func():
#     print('这是func函数')
#     return 'hello'
# ret=func(3,5)
# print(ret)

# 质数
# for i in range(2,11):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,'是质数')

# 数字倒序
a=int(input('请输入一个整数：'))
b=0
while a!=0:
    b=b*10+a%10
    a//=10
print(b)