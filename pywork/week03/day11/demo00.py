'''
私有变量
'''
# class A():
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
# class B(A):
#     pass
# a=A('张三',28)
# print(a.__age)    # 报错
# b=B('李四',19)
# print(b.name)
# print(b.__age)    # 报错

'''
复写
'''
# class A():
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
# class B(A):
#     def __init__(self,name,age,sex):
#         self.sex=sex
#         super().__init__(name,age)
# b=B('张三',19,'男')
# print(b.name)

'''
钻石继承
'''
# class A():
#     def f(self):
#         print('A')
# class B(A):
#     def f(self):
#         super().f()
#         print('B')
# class C(A):
#     def f(self):
#         super().f()
#         print('C')
# class D(B,C):
#     def f(self):
#         super().f()
#         print('D')
# d=D()
# d.f()

'''
多态
'''
# class Dog():
#     def jiao(self):
#         print('汪')
# class Cat():
#     def jiao(self):
#         print('喵')
# def jiao(a):
#     a.jiao()
# c=Cat()
# d=Dog()
# jiao(c)
# jiao(d)