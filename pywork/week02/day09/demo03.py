'''
self--对象本身
哪个对象调用方法或属性，self就是这个对象（id相同）
'''
class Human():
    def eat(self):
        print('人在吃饭')
        print(id(self))
    def study(self):
        print('人在学习')
        print(id(self))
zs=Human()
zs.eat()
print(id(zs))

ls=Human()
ls.study()
print(id(ls))