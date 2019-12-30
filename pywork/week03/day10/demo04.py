# class A():
#     def setAge(self,age):
#         self.__age=age
#     def __str__(self):
#         return str(self.__age)    # 报错 'A' object has no attribute '_A__age'
# a=A()
# a.__age=100
# print(a.__dict__)
# print(a)    # 报错

class A():
    def __init__(self,age):
        self.__age=age
    def setAge(self,age):
        self.__age=age
    def __str__(self):
        return str(self.__age)
a=A(1)
a.__age=100
print(a.__dict__)
print(a._A__age)
a._A__age=99
print(a.__dict__)