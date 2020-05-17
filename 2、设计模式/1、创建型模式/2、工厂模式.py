#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 2、工厂模式.py
@Time: 2020/5/15 11:08
@user：liuhuan   
"""

"""
工厂模式是一个在软件开发中用来创建对象的设计模式
工厂模式包含一个超类，这个超类提供了一个抽象画的接口来创建一个特定类型的对象，而不是决定哪个对象可以被创建。
为了实现此方法，需要创建一个工厂类创建并返回

当程序运行输入一个“类型”的时候，需要创建于此相应的对象，这就要用到工厂模式。在如此情形中，实现代码基于工厂模式，可以达到可扩展，可维护的代码，当增加一个新的类型，不在需要修改已存在的类，只增加能够产生新类型的子类。

简短的说：当以下情形可以用到工厂模式：
1、不知道用户想要创建什么样的对象
2、当你想要创建一个可扩展的关联在创建类与支持创建对象的类之间。

示例：
    1.有一个Person，包含获取名字，性别的方法。有两个子类male和female，可以打招呼，还有一个工厂类。
    2.工厂类有一个方法名getPerson有两个输入参数，名字和性别
    3.用户使用工厂类，通过调用getPerson方法
在程序运行期间，用户传递性别给工厂，工厂创建一个与性别有关的对象。因此工厂类在运行期，决定了哪个对象应该被创建。

"""
# 基类
class Person():
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

#
class Male(Person):
    def __init__(self,name):
        # super().__init__()
        print(name)

class Female(Person):
    def __init__(self,name):
        # super().__init__()
        print(name)

class Factory():
    def getPerson(self,name,gender):
        if gender == "M":
            return Male(name)
        if gender =="F":
            return Female(name)

if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Waltz","M")