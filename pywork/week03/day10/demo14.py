'''
实例化方法--只有实例化之后才可以使用的方法，该方法的第一个形参一定是对象本身
'''
class A():
    num=10
    def hehe(self):
        print('我是实例方法，也叫对象方法')
    @classmethod
    def haha(cls):
        print('我是类方法，我的第一个参数代表的是类，A')
        print(cls.num)
    @staticmethod
    def heihei():
        print('我是静态方法，跟这个类没有太多血缘关系')
a=A()
a.hehe()
A.hehe(a)    # 用类名访问对象方法，第一个参数如果传过来的是对象，就可以
A.haha()
a.haha()    # 传进去的参数，虽然是对象，但我知道它属于哪个类
A.heihei()
a.heihei()