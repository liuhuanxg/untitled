'''
若子类中有自己的跟父类相同的方法，它就用自己的
若没有，用父类的
若有还想用父类的，可使用super()方法
'''
class Animal():
    def __init__(self,name,age):    # 重载、重写、复写、覆盖
        self.name=name
        self.age=age
class Cat(Animal):
    def __init__(self,name,age,velocity):
        self.v=velocity
        super().__init__(name,age)
    def jiao(self):
        print('喵喵喵，速度{}'.format(self.v))
class Dog(Animal):
    # def __init__(self,name,age,height):
    #     self.h=height
    #     super(Dog, self).__init__(name,age)
    def jiao(self):
        # print('汪汪汪，身高{}'.format(self.h))
        print('汪汪汪')
c=Cat('波斯',3,200)
d=Dog('京巴',4)
c.jiao()
d.jiao()