# def p(n):
#     print(n)
#     if n==1:
#         return
#     p(n-1)
#     print("--heihei--")
# p(4)

#p(4)-->p(3)-->p(2)-->p(1)

#p(1)    1
#p(2)    2    1     --heihei--
#p(3)    3    2    1   --heihei--    --heihei--


#当可迭代对象中没有元素，如果指定了default关键字参数，那么就返回default参数的值。这种情况如果没有指定default参数,程序会报错：ValueError: max() arg is an empty sequence；
# list1=[4,6,3,7,9,1,-9,-10]
list1=[]
dict1={'12':2,'4':1}
# print(max(dict1,key=abs))
print(max(list1,default=2))

# l=lambda x:x*2
# s=l(2)
# print(s)

# a = 512
# b = 512
#
# def func():
#     b = 512
#     c = 512
#     print(b is c)
#     print(a is b)
#     print(a is c)
#     # print(b is c)
# func()

import dis

# a = 257
# def main():
#     b = 257  # 第6行
#     c = 257  # 第7行
#     print(b is c)  # True
#     print(a is b)  # False
#     print(a is c)  # False
#
# main()

# from sys import getsizeof,getrefcount
# a = [1,2]

# print(a)
# print(a)
# print(a)
# print(a)
# b = a
# print(getrefcount(a))   #查看某个变量的引用次数


# list1=[]
# for i in range(5):
#     def func(x):
#         return i**x
#     list1.append(func)

# print(i)
# print(list1[0](2))
# print(list1[1](2))
# print(list1[2](2))

list2=[]

# for i in range(5):
#     def func(x,i=i ):
#         return i ** x
#     list2.append(func)
# print(i)
# print("list2",list2)
# print(list2[0](2))
# print(list2[2](2))

# list3=[]
# def func(x,i=3):
#     print(i)
#
# list3.append(func)
# print(list3[0])
#
# la=lambda x:x
# print(la,id(la))
# print(abs)



# class Person(object):
#     _instance=None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance=object.__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         print(111)
# p=Person()

# 1、下面程序的输出结果是什么？为什么会是这种结果？
# class Person():
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#         return object.__new__(cls)
#
#     def __init__(self):
#         print("__init__")
#
#     def __del__(self):
#         print("__del__")
# p=Person()
# print("--finish")

# 2、下面程序的输出结果是什么？为什么会是这种结果？
# class Person():
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#         return object.__new__(cls)
#
#     def __init__(self):
#         print("__init__")
#
#     def __del__(self):
#         print("__del__")
# def func():
#     p=Person()
# func()
# print("--finish")


 # 3、下面程序的输出结果是什么？为什么会是这种结果？
# class Person():
#     def __new__(cls, *args, **kwargs):
#         print("__new__")
#
#     def __init__(self):
#         print("__init__")
#
#     def __del__(self):
#         print("__del__")
# def func():
#     p=Person()
# func()
# print("--finish--")

#4、使用递归实现阶乘、斐波那契数列。



#5、六大基本数据类型的特点。哪些是可变的？哪些是不可变？哪些是有序？哪些是无序？



#6、面向对象。编写一个类，尽可能多的编写函数类型，每个函数的复杂性不要求，可以使用print()表示。
#(1)、要求函数包括魔术方法，实例方法，类方法，静态方法。
#(2)、写出类中的每个函数的调用方法。并编写注释说明调用方法。
# 如:
class Person():
    def __new__(cls, *args, **kwargs):  #魔术方法，在...时候调用
        print("__new__")
        return object.__new__(cls)

    @classmethod
    def show(cls):#类方法，第一个参数是类本身，调用方式是:.....
        print(111)

    @staticmethod
    def run():   #静态方法，没有默认参数，调用方式是.....
        print(2222)
        print('python')