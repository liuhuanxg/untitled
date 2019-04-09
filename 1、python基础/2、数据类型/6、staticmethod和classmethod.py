
"""
python中有三个方法，静态方法(staticmethod)和类方法
(classmethod)和实例方法

"""
def  foo(x):
    print("excuting foo(%s)"%(x))

class A(object):
    def foo(self,x):
        print("excuting foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("excuting static_foo(%s)"%(x))
a=A()
a.foo(11111)   #excuting foo(<__main__.A object at 0x000001F61BC32390>,11111)
a.class_foo(22222)  #executing class_foo(<class '__main__.A'>,22222)
a.static_foo(33333)  #excuting static_foo(33333)

class Father():
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=super(Father,cls).__new__(cls,*args,**kwargs)
        return cls._instance
class Foo(Father):
    pass
f1=Foo()
f2=Foo()
print(f1 is f2)

