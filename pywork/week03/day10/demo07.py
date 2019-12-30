class Animal():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def jiao(self):
        print(self.name+'叫')
    def eat(self):
        print(self.name+'吃')
class Cat(Animal):
    def climb(self):
        print(self.name+'爬树')
class Dog(Animal):
    def swimming(self):
        print(self.name+'游泳')

d=Dog('藏獒',7,'公')
d.eat()
d.jiao()
d.swimming()
c=Cat('波斯猫',4,'母')
c.eat()
c.jiao()
c.climb()

'''
类名.__bases__--查看继承的父类
如果一个类没有继承任何类，默认继承object类
'''
print(Cat.__bases__)
print(Animal.__bases__)