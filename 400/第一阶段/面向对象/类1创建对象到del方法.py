'''
类名：首字母大写，其他遵循驼峰规则，见名知义
属性：见名知义
行为（方法/功能）：见名知义，其他遵循驼峰原则

类：一种数据类型，本身并不占内存空间，跟number,string,boolean等类似，用类创建实例化对象（变量），对象占内存空间

格式：
class  类名（父类列表）：
      属性
      行为

'''
#object:基类或者超类，所有类的父类
# 一般没有合适的父类就写object
# class Person(object):
#     #定义属性
#     name=''
#     age=0
#     height=0
#     weight=0
#     #定义方法（定义函数）
#     #注意：方法的参数必须以self当第一个参数
#     #self代表类的实例（某个对象）
#     def run(self):
#         print('run')
#     def eat(self,food):
#         print('eat'+food)
# a=Person()
# a.eat('food')


'''
2、使用类实例化对象
格式：对象名=类名（参数列表）
注意：没有参数，小括号也不能省略
'''
# 实例化一个对象
'''
class Person(object):
    name=''
    age=0
    height=0
    weight=0
    def run(self):
        print('run')
    def eat(self,food):
        print('eat'+food)
    def openDoor(self):
        print('我已经打开了冰箱门')
    def fillEle(self):
        print('我已经把大象装进冰箱了' )
    def clossDoor(self):
        print('关门')
per1=Person()
print(per1)
per2=Person()
print(per2)
'''

# 3、访问对象的属性与方法:
'''
访问属性
格式：对象名，属性名
赋值：对象名.属性名=新值
'''
'''
class Person(object):
    name=''
    age=0
    height=80
    weight=0
    def run(self):
        print('run')
    def eat(self,food):
        print('eat '+food)
    def openDoor(self):
        print('我已经打开了冰箱门')
    def fillEle(self):
        print('我已经把大象装进冰箱了' )
    def clossDoor(self):
        print('关门')
per=Person()
per.name='tom'
per.age=18
per.weight=19
# per.height=100
print(per.name,per.age,per.weight,per.height)
'''
'''
访问方法：
格式：对象名，方法名（参数列表）
'''
# per.fillEle()
# per.clossDoor()
# per.eat('apple')

#问题：目前python所有的对象都是一样的。


'''
4、对象的初始状态：

'''

'''
1、构造函数：__init__(self)在使用类创建对象的时候自动调用
注意：如果不显示的写出构造函数，默认会自动添加一个空的构造函数。
'''
'''
class Person(object):
    def __init__(self, name, age, weight, height):
        #定义属性
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def run(self):
        print('run')
    def eat(self,food):
        print('eat '+food)

per1=Person('hanmeimei',12,23,56)
print(per1.name,per1.height)
'''


'''
5、self 代表类的实例，并不是类
哪个对象调用方法，那么该方法中的self就代表那个对象

self.__class__  代表类名
'''
# class Person(object):
#     def __init__(self, name, age, weight, height):
#         self.name=name
#         self.age=age
#         self.weight=weight
#         self.height=height
#         pass
#     def run(self):
#         print('run')
#     def eat(self,food):
#         print('eat '+food)
#     def say(self):
#         print('我是：%s,我今年%d岁，身高：%d,体重：%d'%(self.name,self.age,self.height,self.weight))
#     def play(a):
# #     self不是关键字，但一般都是用self，也可以用其他的，帅的人都用self
#         print('play '+a.name)
# per2=Person('xx',12,30,40)
# #此时self代表per2
# per2.say()
# per2.play()
# per3=Person('xigua',20,45,67)
# #此时self代表per3
# per3.say()

'''
析构函数：释放对象时执行。(自动执行）
def __del__(self)
'''
class Person(object):
    def __init__(self, name, age, weight, height):
        #定义属性
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        print('这里是init')
    def run(self):
        print('run')
    def eat(self,food):
        print('eat '+food)
    def __del__(self):
        print('这里是析构函数。')
per4=Person('西瓜',22,177,72)
# del per4
#释放对象
print(per4.name)
# 对象释放以后就不能在访问了


#在函数里定义的对象，会在函数结束时自动释放，这样就可以用来减少内存空间的浪费
