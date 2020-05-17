import re
#使用装饰器
"""
def singleton(cls):
    instances={}
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls]=cls(*args,**kwargs)
        return instances[cls]
    return wrapper

@singleton
class Foo(object):
    pass
foo1=Foo()
foo2=Foo()
print(foo1 is foo2)
"""

a = "abbbccc"
print(re.sub(r'b+', 'b', a))


#第二种使用基类New
"""
class SingLeton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super(SingLeton,cls).__new__(cls,*args,**kwargs)
        return cls._instance

class Foo(SingLeton):
    pass

foo1=Foo()
foo2=Foo()
print(foo1 is foo2)
"""

#第三种：元类，元类是用于创建对象的类，类对象创建实例对象时一定要调用call方法时候保证始终创建一个实例，type是python的元类

class Singleton(type):

    def __call__(cls):
        if not hasattr(cls,'_instance'):
            cls._instance = super().__call__()
        return cls._instance
class Foo(object):
    __metaclass__ = Singleton

foo1 = Foo()
foo2 = Foo()
print(foo1 is foo2,id(foo1),id(foo2),111)


# class Father():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,"_instance"):
#             cls._instance=super(Father,cls).__new__(cls,*args,**kwargs)
#         return cls._instance
#
# class Foo(Father):
#     pass
#
# f1=Foo()
# f2=Foo()
# print(f1 is f2)

class Father():
    def __new__(cls,*args,**kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=super(Father,cls).__new__(cls,*args,**kwargs)
        return cls._instance

class Foo(Father):
    pass

f1=Foo()
f2=Foo()
f3 = Father
f4 = Father
print(id(f1))
print(id(f2))
print(f1 is f2)