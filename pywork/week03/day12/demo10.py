'''
@property装饰器--把一个方法的调用方式变为属性调用方式（将一个方法当成一个属性使用）。只能在面向对象中使用。
只能修饰不带参数的方法。
@age.setter--是@property装饰器的副产品，用来修饰setter方法。
'''
# class A():
#     def __init__(self,name):
#         self.name=name
#     @property    # 把方法作为属性使用
#     def age(self):
#         return self.__age    # 属性不能与函数名重名
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
#
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
#         self._r=r
#     @property
#     def c(self):
#         return 2*pi*self._r
#     @property
#     def area(self):
#         return pi*self._r*self._r
# y=Circle(1)
# print(y.c)
# print(y.area)

class Person():
    def __init__(self,name,w,h):
        self.name=name
        self.weight=w
        self.height=h
    @property
    def bmi(self):
        return self.weight/(self.height**2)
p=Person('吕佳',48,1.63)
print(p.bmi)