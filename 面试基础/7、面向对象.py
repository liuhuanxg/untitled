#面向对象的三大特征：封装、继承、多态
#python一切皆对象
#python支持单继承
#类变量是可变变量
'''
class Father():
    name='father'

F=Father()
print(F.name)
F.name='fa'
print(F.name)
'''


class Father():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def xianshi(self):
        print(self.name,self.age)
class Mother(Father):
    def __init__(self,name,age):
        Father.__init__(self,name,age)

class Son(Mother):
    def __init__(self,name,age,score):
        Father.__init__(self,name,age)
        self.score=score
    def sc(self):
        print(self.score)
son=Son('xiaoming',19,80)
son.xianshi()
son.sc()

"""
七、多态：多态就是不同的对象可以调用相同的方法然后得到不同的结果，类似接口类，在python中处处体现多态，比如不管是列表还是字符串还是数字都可以使用+和*。
"""


"""
八、封装：封装就是把类中的属性和方法定义为私有的，方法就是在属性名或方法名前加双下划线，而一旦这样定义了属性或方法名后，python会自动将其转换为_类名__属性名（方法名）的格式，在类的内部调用还是双下划线加属性名或方法名，在类的外部调用就要用_类名__属性名(方法名)。父类的私有属性和方法，子类无法对其进行修改。
"""

"""

"""