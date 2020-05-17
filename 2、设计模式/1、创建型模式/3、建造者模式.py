#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 3、建造者模式.py
@Time: 2020/5/15 13:37
@user：liuhuan   
"""

"""
将一个复杂对象的构建与他的表示分离，使得同样的构建过程可以创建不同的表示

相关模式：思路和模板方法的模式很像，模板方法是封装算法流程，对某些细节提供接口由子类修改，建造者模式更为高层一点，将所有细创建节交由子类实现。

与工厂模式的不同之处：
    1、想要创建一个复杂对象(对象由多个部分构成，切对象的创建要经过多个不同的步骤，这些步骤还需要遵从特定的顺序)。
    2、要求一个对象能有不同的表现，并希望将对象的构造与表现解耦。
    3、想要在某个时间点创建对象，但在稍后的时间点再访问

示例：
1.有一个接口类，定义创建对象的方法。一个指挥员类，接受创造者对象为参数。两个创造者类，创建对象方法相同，内部创建可自定义
2.一个指挥员，两个创造者（瘦子 胖子），指挥员可以指定由哪个创造者来创造

"""
from abc import ABCMeta, abstractmethod

class Builder():
    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_left_arm(self):
        pass

    @abstractmethod
    def draw_right_arm(self):
        pass

    @abstractmethod
    def draw_left_foot(self):
        pass

    @abstractmethod
    def draw_right_foot(self):
        pass

    @abstractmethod
    def draw_head(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass

class Thin(Builder):
    def draw_left_arm(self):
        print("画左手")

    def draw_right_arm(self):
        print("画右手")

    def draw_left_foot(self):
        print("画左脚")

    def draw_right_foot(self):
        print("画右脚")

    def draw_head(self):
        print("画头")

    def draw_body(self):
        print("画瘦身体")


class Fat(Builder):
    def draw_left_arm(self):
        print("画左手")

    def draw_right_arm(self):
        print("画右手")

    def draw_left_foot(self):
        print("画左脚")

    def draw_right_foot(self):
        print("画右脚")

    def draw_head(self):
        print("画头")

    def draw_body(self):
        print("画胖身体")

class Director():
    def __init__(self,person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_left_foot()
        self.person.draw_right_foot()
        self.person.draw_head()
        self.person.draw_body()

if __name__ == '__main__':
    thin = Thin()
    fat = Fat()
    director_thin = Director(thin)
    director_thin.draw()
    director_fat = Director(fat)
    director_fat.draw()