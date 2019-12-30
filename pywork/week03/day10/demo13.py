'''
多态
'''
class Dog():
    def jiao(self):
        print('汪汪')
class Cat():
    def jiao(self):
        print('喵喵')
class Pig():
    def jiao(self):
        print('哼哼')
def hehe(a):
    a.jiao()
d=Dog()
c=Cat()
p=Pig()
# 若不知道d,c,p对象是什么类型的对象，就不知道会执行哪个
# 这就是多态
hehe(d)
hehe(c)
hehe(p)

class Ali():
    def pay(self,money):
        print('阿里支付:',money)
class WChat():
    def pay(self,money):
        print('微信支付:',money)
class Person():
    def comsume(self,x,money):
        x.pay(money)
a=Ali()
w=WChat()
zs=Person()
zs.comsume(a,100)
zs.comsume(w,200)