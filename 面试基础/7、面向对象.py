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

