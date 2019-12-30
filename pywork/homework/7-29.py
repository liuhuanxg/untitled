# Python 0715 吕佳
'''
形如：__变量名--私有变量
'''
# class Girl():
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def show(self):
#         print(self.name,self.__age)
# zs=Girl('张三',18)
# zs.show()
# print(zs.name)
# print(zs.__age)    # 报错

# class Girl():
#     def __init__(self):
#         pass
#     def setAge(self,age):
#         if age<0 or age>95:
#             print('错误')
#             self.age=0
#         else:
#             self.age=age
#     def getAge(self):
#         return self.age
# zs=Girl()
# zs.setAge(20)
# print(zs.getAge())
#
# # 可通过对象添加属性将之前的值进行覆盖
# # 解决办法：使用私有属性
# zs.age=-9
# print(zs.getAge())
# zs.setAge(200)
# print(zs.getAge())

'''
类外部的zs.__age=99中，__age不是类中的那个私有变量，是一个新的变量
print(zs.__dict__)中，'_Girl__age': 21才是私有变量
'''
# class Girl():
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def setAge(self,age):
#         if age<0 or age>95:
#             print('错误')
#             self.__age=0
#         else:
#             self.__age=age
#     def getAge(self):
#         return self.__age
# zs=Girl('张三',18)
# zs.setAge(21)
# print(zs.getAge())
# print(zs.__dict__)
#
# zs.__age=99
# print(zs.getAge())
# print(zs.__dict__)

# class A():
#     def setAge(self,age):
#         self.__age=age
#     def __str__(self):
#         return str(self.__age)
# a=A()
# a.__age=100
# print(a.__dict__)
# print(a)

# class A():
#     def __init__(self,age):
#         self.__age=age
#     def setAge(self,age):
#         self.__age=age
#     def __str__(self):
#         return str(self.__age)
# a=A(1)
# a.__age=100
# print(a.__dict__)
# print(a._A__age)
# a._A__age=99
# print(a.__dict__)

# class Phone():
#     def test(self):
#         print('test1')
#     def __test1(self):
#         print('test1')
# x=Phone()
# x.test()
#
# # 私有方法，无法调用
# x.__test1()

# class Phone():
#     def __phone(self):
#         print('正在拨打电话')
#     def phone(self,m):
#         if m>=30:
#             self.__phone()
#         else:
#             print('请先交费30元以上，才可以打电话')
# x=Phone()
# x.phone(36)

# class Animal():
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def jiao(self):
#         print(self.name+'叫')
#     def eat(self):
#         print(self.name+'吃')
# class Cat(Animal):
#     def climb(self):
#         print(self.name+'爬树')
# class Dog(Animal):
#     def swimming(self):
#         print(self.name+'游泳')
# d=Dog('藏獒',7,'公')
# d.eat()
# d.jiao()
# d.swimming()
# c=Cat('波斯猫',4,'母')
# c.eat()
# c.jiao()
# c.climb()
'''
类名.__bases__--查看继承的父类
如果一个类没有继承任何类，默认继承object类
'''
# print(Cat.__bases__)
# print(Animal.__bases__)

'''
方法的重写
'''
# class A():
#     def hehe(self):
#         print('A:呵呵')
# class B(A):
#     def hehe(self):
#         print('B:呵呵')
# a=A()
# b=B()
# a.hehe()
# b.hehe()

'''
若子类中有自己的跟父类相同的方法，它就用自己的
若没有，用父类的
若有还想用父类的，可使用super()方法
'''
# class Animal():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class Cat(Animal):
#     def __init__(self,name,age,velocity):
#         self.v=velocity
#         super().__init__(name,age)
#     def jiao(self):
#         print('喵喵喵，速度：{}'.format(self.v))
# class Dog(Animal):
#     def jiao(self):
#         print('汪汪汪')
# c=Cat('波斯',3,200)
# d=Dog('京巴',4)
# c.jiao()
# d.jiao()

# class A():
#     num=3
#     __num1=2
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# class B(A):
#     num=10
#     def __init__(self,x,y,z):
#         self.z=z
#         super().__init__(x,y)
# b=B(1,2,3)
# print(b.x)
# print(B.num)
# print(A.num)
#
# # print(B.__num)    # 报错
# # super()还可以从外部使用，需要传递类名（本类）和对象名
# print(super(B,b).num)

'''
多继承
'''
# class A():
#     def t(self):
#         print('A:t1')
# class B():
#     def t(self):
#         print('B:t2')
# class C(A,B):
#     def t(self):
#         print('C:t3')
# c=C()
# c.t()

# class A():
#     def tx(self):
#         print('A:t1')
# class B():
#     def tx(self):
#         print('B:t2')
# class C(A,B):
#     def t(self):
#         print('C:t3')
# c=C()
# c.tx()

# class A():
#     def tx(self):
#         print('A:t1')
# class B():
#     def tx(self):
#         print('B:t2')
# class C(B,A):
#     def t(self):
#         print('C:t3')
# c=C()
# c.tx()

# class A():
#     def func(self):
#         print('A开始')
#         print('A结束')
# class B(A):
#     def func(self):
#         print('B开始')
#         super().func()
#         print('B结束')
# class C(A):
#     def func(self):
#         print('C开始')
#         super().func()
#         print('C结束')
# class D(B,C):
#     def func(self):
#         print('D开始')
#         super().func()
#         print('D结束')
# print(D.mro())
# d=D()
# d.func()

# class A():
#     def __init__(self):
#         print('A开始')
#         print('A结束')
# class B(A):
#     def __init__(self):
#         print('B开始')
#         super().__init__()
#         print('B结束')
# class C(A):
#     def __init__(self):
#         print('C开始')
#         super().__init__()
#         print('C结束')
# class D(B,C):
#     def __init__(self):
#         print('D开始')
#         super(D, self).__init__()
#         print('D结束')
# print(D.mro())
# d=D()

# class A():
#     def __init__(self):
#         print('A')
#         super(A, self).__init__()
# class B():
#     def __init__(self):
#         print('B')
#         super().__init__()
# class C(A,B):
#     def __init__(self):
#         print('C')
#         super().__init__()
# print(C.mro())
# c=C()

'''
多态
'''
# class Dog():
#     def jiao(self):
#         print('汪汪汪')
# class Cat():
#     def jiao(self):
#         print('喵喵喵')
# class Pig():
#     def jiao(self):
#         print('哼哼哼')
# def hehe(a):
#     a.jiao()
# d=Dog()
# c=Cat()
# p=Pig()
# # 若不知道d,c,p对象是什么类型的对象，就不知道会执行哪个
# # 这就是多态
# hehe(d)
# hehe(c)
# hehe(p)

# class Ali():
#     def pay(self,money):
#         print('阿狸支付',money)
# class WChat():
#     def pay(self,money):
#         print('微信支付',money)
# class Person():
#     def comsume(self,x,money):
#         x.pay(money)
# a=Ali()
# w=WChat()
# zs=Person()
# zs.comsume(a,100)
# zs.comsume(w,200)

# class A():
#     num=10
#     def hehe(self):
#         print('我是实例方法，也叫对象方法')
#     @classmethod
#     def haha(cls):
#         print('我是类方法，我的第一个桉树代表的是类，A')
#         print(cls.num)
#     @staticmethod
#     def heihei():
#         print('我是静态方法，跟这个类没有太多血缘关系')
# a=A()
# a.hehe()
# A.hehe(a)# 用类名访问对象方法，第一个参数如果传过来的是对象，就可以
# A.haha()
# a.haha()
# A.heihei()
# a.heihei()
# ------------------------------------------------------
# 作业题
# 静态方法类方法使用
# 植物大战僵尸
# class Game(object):
#     top_score=0
#     def __init__(self,player_name):
#         self.player_name=player_name
#     @staticmethod
#     def show_help():
#         print('提示消息：小心让僵尸吃掉你的脑子哦')
#     @classmethod
#     def show_top_score(cls):
#         print('历史记录%d'%cls.top_score)
#     def start_game(self):
#         print('%s开始游戏啦...'%self.player_name)
# Game.show_help()
# Game.show_top_score()
# game=Game('小明')
# game.start_game()

# 多态
# class Dog(object):
#     def __init__(self,name):
#         self.name=name
#     def game(self):
#         print('%s 蹦蹦跳跳的玩耍...'% self.name)
# class XiaoTianDog(Dog):
#     def game(self):
#         print('%s飞到天上去玩耍...'%self.name)
# class Person(object):
#     def __init__(self,name):
#         self.name=name
#     def game_with_dog(self,dog):
#         print('%s和%s快乐的玩耍...'%(self.name,dog.name))
#         dog.game()
# xt_dog=XiaoTianDog('哮天犬')
# els=Person('二郎神')
# els.game_with_dog(xt_dog)