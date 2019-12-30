'''
类外部的zs.__age=99中，__age不是类中的那个私有变量，是一个新的变量
print(zs.__dict__)中，'_Girl__age': 21才是私有变量
'''
class Girl():
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def setAge(self,age):
        if age<0 or age>95:
            print('错误')
            self.__age=0
        else:
            self.__age=age
    def getAge(self):
        return self.__age
zs=Girl('张三',18)
zs.setAge(21)
print(zs.getAge())
print(zs.__dict__)

# 之前的值没有被覆盖
zs.__age=99
print(zs.getAge())
print(zs.__dict__)