
'''
重写:__repr__     是给机器用的，在python解释器里边直接敲对象名再回车后调用的方法。
与__str__函数    在调用print打印对象时自动调用。是给用户用的，是一个描述对象的方法。
将函数重新写一遍。

'''
'''
class Person(object):
    def __init__(self, name, age, weight, height):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def __str__(self):
        return  '%s-%d-%d-%d'%(self.name,self.age,self.weight,self.height)

per4=Person('西瓜',22,177,72)
print(per4)
'''
#优点：当一个对象的属性值有很多，并且都需要打印，重写了__str__方法后，简化了代码。



# 作业：人开枪射击子弹


class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox=bulletBox
    def shoot(self):
        if self.bulletBox.bulletCount==0:
            print('没有子弹了')
        else:
            self.bulletBox.bulletCount-=1
            print('剩余子弹：%d'%(self.bulletBox.bulletCount))
class Person(object):
    def __init__(self,gun):
        self.gun=gun
    def fire(self):
        self.gun.shoot()
    def fillBullet(self,count):
        self.gun.bulletBox.bulletCount=count
        #装子弹
class BulletBox(object):
    def __init__(self,count):
          self.bulletCount=count

bulletBox=BulletBox(5)
gun=Gun(bulletBox)
per=Person(gun)
per.fire()
per.fillBullet(3)
per.fire()