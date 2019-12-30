# Python 0715 吕佳

# class Student():
#     name=''
#     def study(self):
#         print(self.name,'去学习两个小时')
#     def eat(self):
#         print(self.name,'去吃饭')
#     def gym(self):
#         print(self.name,'跑步200公里')
# a=Student()
# a.name='lj'
# a.study()
# a.eat()
# a.gym()
#
# b=Student()
# b.name='qwe'
# b.study()
# b.eat()
# b.gym()


# class Dog():
#     def eat(self):
#         print('小狗吃饭')
#     def sleep(self):
#         print('小狗睡觉')
# d=Dog()
# d.eat()
# d.sleep()

'''
self--对象本身
哪个对象调用方法或属性，self就是这个对象（id相同）
'''
# class Human():
#     def eat(self):
#         print('人在吃饭')
#         print(id(self))
#     def study(self):
#         print('人在学习')
#         print(id(self))
# zs=Human()
# zs.study()
# zs.eat()
# print(id(zs))
#
# ls=Human()
# ls.eat()
# ls.study()
# print(id(ls))

'''
__init__()在创建对象的时候自动执行
在__init__()中做初始化操作
'''
# class Student():
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def show(self):
#         print('我叫{}，年龄{}，性别{}'.format(self.name,self.age,self.sex))
# zs=Student('张三',18,'女')
# zs.show()
#
# ls=Student('李四',29,'男')
# ls.show()


# class Student():
#     def __init__(self,name):
#         self.name=name
#     def hehe(self,age):
#         self.age=age
#     def show(self):
#         print('我是{}，年龄{}'.format(self.name,self.age))
# zs=Student('张三')
# zs.show()    # 报错


# class Student():
#     def __init__(self,name):
#         self.name=name
#     def hehe(self,age):
#         self.age = age
#     def show(self):
#         print('我叫{}，年龄{}'.format(self.name,self.age))
# zs=Student('张三')
# zs.hehe(10)
# zs.show()

'''
在类的外部增加属性（不推荐使用）
'''
# class Teacher():
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(self.name,self.age)
# zs=Teacher('张三')
# zs.age=80
# zs.show()
#
# ls=Teacher('李四')
# ls.show()    # 报错


# class Student():
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def show(self):
#         print(self.name,self.age,self.sex)
#     def setAge(self):
#         self.age=19
# zs=Student('张三',23,'男')
# zs.show()
# zs.setAge()
# zs.show()

'''
__str__()函数--打印对象名称是默认调用__str__()方法，默认返回的是对象的内存地址
可重写__str__()打印对象保存的信息
'''
# class Dog():
#     def __init__(self,color,age):
#         self.color=color
#         self.age=age
#     def __str__(self):
#         return '颜色%s 年龄%d'%(self.color,self.age)
# d=Dog('黄色',4)
# print(d)
# b=d
# print(b,type(b))


# class Teacher():
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def __str__(self):
#         return '我叫{}，工资{}'.format(self.name,self.salary)
# a=Teacher('张三',999999)
# print(a)


# from math import pi
# class Circle():
#     def __init__(self,radis):
#         self.radis=radis
#     def area(self):
#         return pi*self.radis*self.radis
#     def c(self):
#         return 2*pi*self.radis
#     def __str__(self):
#         return '我的半径是%d，周长为%.2f，面积为%.2f'%(self.radis,self.c(),self.area())
# a=Circle(5)
# print(a)


# class Sheep():
#     def __init__(self):
#         self.cooktime=0
#         self.status='生的'
#     def cook(self,cook_time):
#         self.cooktime=cook_time
#         if self.cooktime<2:
#             self.status='生的'
#         elif self.cooktime>=2 and self.cooktime<4:
#             self.status='半熟'
#         elif self.cooktime>=4 and self.cooktime<6:
#             self.status='熟了'
#         elif self.cooktime>=6:
#             self.status='老了'
#     def __str__(self):
#         return '烤了%d个小时，状态:%s' % (self.cooktime, self.status)
# s=Sheep()
# s.cook(5)
# print(s)


# class YangRouChuan():
#     def __init__(self):
#         self.cook_time=0
#         self.status='生的'
#     def cook(self,cook_time):
#         self.cook_time+=cook_time
#         if self.cook_time<2:
#             self.status='生的'
#         elif self.cook_time<4:
#             self.status='半熟'
#         elif self.cook_time<6:
#             self.status='熟了'
#         else:
#             self.status='老了'
#     def __str__(self):
#         return '烤了%d个小时，状态%s'%(self.cook_time,self.status)
# s=YangRouChuan()
# s.cook(2)
# print(s)
# s.cook(3)
# print(s)
# s.cook(3)
# print(s)


# class Person():
#     def __init__(self,name,attack_power,hp):
#         self.name=name
#         self.attack_power=attack_power
#         self.hp=hp
#     def attack(self,obj):
#         obj.hp-=self.attack_power
#     def __str__(self):
#         return '我叫{},我还有{}滴血，我的攻击力是{}'.format(self.name,self.hp,self.attack_power)
# class NPC():
#     def __init__(self,name,attack_power,hp):
#         self.name=name
#         self.attack_power=attack_power
#         self.hp=hp
#     def attack(self,obj):
#         obj.hp-=self.attack_power
#     def __str__(self):
#         return '枭雄{},我还有{}滴血，我的攻击力是{}'.format(self.name, self.hp,self.attack_power)
# r=Person('诸葛亮',30,100)
# c=NPC('曹操',25,150)
# r.attack(c)
# c.attack(r)
# print(c)
# print(r)


# class House():
#     def __init__(self,info,area,address):
#         self.info=info
#         self.area=area
#         self.address=address
#         self.furnitures=[]
#     def addFurnitures(self,obj):
#         self.area-=obj.area
#         self.furnitures.append(obj.name)
#     def __str__(self):
#         s1='户型{}，面积{}，地址{}，'.format(self.info,self.area,self.address)
#         s2='室内家具有：'
#         for f in self.furnitures:
#             s2+=f+' '
#         return s1+s2
# class Furniture():
#     def __init__(self,name,area):
#         self.name=name
#         self.area=area
# h1=House('三室一厅',138,'北京大兴')
# bed=Furniture('床',6)
# h1.addFurnitures(bed)
# print(h1)
# table=Furniture('书桌',4)
# h1.addFurnitures(table)
# print(h1)
# sofa=Furniture('沙发',10)
# h1.addFurnitures(sofa)
# print(h1)

'''
类属性和实例属性
'''
# class People():
#     tax=0.01
#     def __init__(self,salary):
#         self.salary=salary
#     def pay(self):
#         return self.salary*People.tax
# a=People(10000)
# b=People(20000)
# # print(a.pay())
# # print(b.pay())
# # People.tax=0.02
# # print(a.pay())
# # print(b.pay())
# # print(id(a.tax))
# # print(id(People.tax))
# a.tax=0.07
# print(People.tax)

# class People():
#     tax=0.01
#     def __init__(self,salary):
#         self.salary=salary
#     def pay(self):
#         return self.salary*People.tax
# a=People(10000)
# b=People(20000)
# # 只要有=，就是一个新开辟的变量了，与类变量无关了
# # a.tax=a.tax+1 混合使用，前面的tax是对象属性，后边的那个是类属性
# a.tax+=0.01
# print(a.tax,id(a.tax))
# print(People.tax,id(People.tax))
# # 类变量变了，他也不变
# People.tax=200
# print(a.tax)
# # 删除a的属性，就使用类的
# delattr(a,'tax')
# print(a.tax)

# class A():
#     def __init__(self):
#         self.tax=0.1
# x=A()
# print(x.tax)
# delattr(x,'tax')
# print(x.tax)

# class A():
#     books=['三国','西游记']
#     def __init__(self,name):
#         self.name=name
# x=A('张三')
# y=A('李四')
# x.books[0]='水浒传'
# print(x.books)
# print(y.books)
# print(A.books)
#
# x.books=['红楼梦','大秦帝国']
# print(x.books)
# print(y.books)
# print(A.books)
# ------------------------------------------------------------------------------
# 作业题
# 面向对象中 属性的练习
"""
邓超 体重 75.0 公斤
邓超每次 奔跑 会减肥 0.1 公斤
邓超每次 吃东西 体重增加 0.5 公斤
"""
# class Person():
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#     def __str__(self):
#         return '我的名字叫%s，体重公斤%.2f'%(self.name,self.weight)
#     def run(self):
#         self.weight-=0.1
#     def eat(self):
#         self.weight+=0.5
# r=Person('邓超',75)
# r.run()
# print(r)
# r.eat()
# print(r)
# r.eat()
# print(r)

# 两个类配合使用练习

"""
需求
狙击手 麦克 有一把 狙M99
麦克 可以 开火
狙M99 能够 发射 子弹
狙M99 装填 装填子弹 —— 增加子弹数量
"""
class Gun():
    def __init__(self,model):
        self.model=model
        self.bullet_count=0
    def add_buttle(self,count):
        self.bullet_count+=count
    def shoot(self):
        if self.bullet_count<=0:
            print('没有子弹了')
            return
        self.bullet_count-=1
        print('%s发射子弹[%d]'%(self.model,self.bullet_count))
class Sniper():
    def __init__(self,name):
        self.name=name
        self.gun=None
    def fire(self):
        if self.gun is None:
            print('[%s]还没有枪'%self.name)
            return
        print('冲啊  [%s]'%self.name)
        self.gun.add_buttle(50)
        self.gun.shoot()
m99=Gun('M99')
m99.shoot()
sniper=Sniper('麦克')
sniper.gun=m99
sniper.fire()