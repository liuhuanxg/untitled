# Python 0715 吕佳
# class A():
#     num=0    # 类属性，也叫静态属性
#     def __init__(self,name):
#         A.num+=1    # 每定义一个对象，计数器加1
#         self.name=name
#     def __del__(self):
#         A.num-=1
#         print(self.name,'被删除，还剩下{}个对象'.format(A.num))
# a=A('张三')
# b=A('李四')
# c=A('王五')
# print(A.num)
# del a    # 自动调用__del__()
# del b
# del c

'''
__call__()方法
可以让类的实例具有类似于函数的行为，进一步模糊了函数和对象之间的概念
对象后面加括号，就像函数调用一样触发执行。对象()或类()()
'''
# class A():
#     def __init__(self,num):
#         self.num=num
#     def __call__(self,n):
#         return self.num*n
# a=A(7)
# print(a(9))
# print(A(3)(7))

# class Fib():
#     def __call__(self,month):
#         lst=[]
#         a,b=1,1
#         n=1
#         while n<=month:
#             lst.append(a)
#             a,b=b,a+b
#             n+=1
#         return lst
# f=Fib()
# for i in range(1,10):
#     print(f(i))

# class Fib():
#     def __call__(self,month):
#         a,b=0,1
#         n=1
#         while n<=month:
#             a,b=b,a+b
#             n+=1
#         return a
# f=Fib()
# m=int(input('请输入：'))
# print(f(m))

'''
__str__()方法
__repr__()方法
改变对象的字符串显示
是__str__()方法的备胎，如果找不到__str__()就会找它
%r默认调用__repr__()
repr()默认调用__repr__()
'''
# class Per():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return '%s:%d'%(self.name,self.age)
#     def __repr__(self):
#         return '我叫{}，年龄{}'.format(self.name,self.age)
# a=Per('张三',19)
# print(a)
# print(str(a))
# print('%s'%a)
# print('%r'%a)
# print(repr(a))

'''
__new__()方法--实例化方法
在实例化对象时自动触发
至少有一个cls参数接收当前类，返回一个对象实例
先触发__new__才会触发__init__
'''
# class Stu():
#     # 实例化
#     def __new__(cls, *args, **kwargs):
#         print('11111111111111111')
#         # 如果不写这句，就没有创建对象，只打印111，不打印222。调用父类的__nuw__()方法就可以创建对象了
#         # return object.__new__(cls)
#     def __init__(self,name,age):
#         print('22222222222222222')
#         self.name=name
#         self.age=age
# zs=Stu('张三',19)
# print(zs.name)

'''
is与==的区别
is比较两个对象的id值是否相等，是否指向同一个内存地址。
==比较的是两个对象的内容是否相等，默认调用对象的__eq__()方法。
继承自object的__eq__方法比较两个对象的id。
对于自定义对象一般认为对象的值相同就同一个对象，因此需要重写__eq__()方法。
'''
# class Stu():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __eq__(self, other):
#         return self.__dict__==other.__dict__
# a=Stu('张三',19)
# b=Stu('李四',23)
# c=Stu('张三',19)
# print(a==c)
#
# d=[]
# d.append(a)
# if c not in d:
#     d.append(c)
# print(d)

'''
__hush__()方法--哈希/散列
将一个不定长的输入，通过哈希函数变换成一个定长的输出，即哈希值。
hash值是对象的id值的十六分之一。
'''
# class Stu():
#     def __init__(self,name):
#         self.name=name
# a=Stu('张三')
# b=Stu('李四')
# c=Stu('王五')
# s={a,b,c}
# print(s)
# print(hash(a))
# print(id(a)/16)

# class Stu():
#     def __init__(self,name):
#         self.name=name
#     def __eq__(self, other):
#         print('222')
#         return self.name==other.name
#     def __hash__(self):
#         print('111')
#         return hash(self.name)
# a=Stu('张三')
# b=Stu('李四')
# c=Stu('张三')
# print(id(a))
# print(id(b))
# print(id(c))
# print(a==c)
# d={a,b,c}
# print(d)

'''
检测一个类，是否为另一个类的子类
issubclass(被检测类，父类)，若一次判断多个父类，有一则为真
isinstance(对象，类)，若一次判断多个类，有一则为真
'''
# class A():
#     pass
# class B(A):
#     pass
# print(issubclass(B,A))
# a=A()
# print(isinstance(a,A))

'''
反射方法
hasattr()--判断是否有此变量，返回值为bool类型
getattr()--获取属性值或者获取方法变量的地址，返回值为值
delattr()--删除类或者对象的属性或方法
setattr()--给类或者对象设置属性或者方法
'''
class A():
    dog=0
    def hehe(num):
        print(num)
# setattr(A,'dog',90)
# print(getattr(A,'dog'))
# setattr(A,'cat',10)
# print(A.__dict__)

# a=A()
# print(a.__dict__)
# setattr(a,'haha',1999)
# print(a.__dict__)
# a.hehe=2022
# print(a.__dict__)


# print(getattr(A,'dog'))
# f=getattr(A,'hehe')
# f(1)
# delattr(A,'dog')
# print(hasattr(A,'dog'))

# class A():
#     def f1(self):
#         print('我是f1')
#     def f2(self):
#         print('我是f2')
#     def f3(self):
#         print('我是f3')
# print(A.__dict__)
# a=A()
# f=input('请输入你想要调用的方法：')
# if hasattr(A,f):
#     fc=A.__dict__.get(f)
#     fc(a)
# else:
#     print('没有',f)

'''
反射自己模块中的属性和函数
'''
# import sys
# zhutou=1299
# def func():
#     print('aaaaaaaaaaaaaaaa')
#
# print(sys.modules)
# print(sys.modules['__main__'])
#
# x=getattr(sys.modules['__main__'],'zhutou')
# print(x)
# x=getattr(sys.modules['__main__'],'func')
# x()

'''
反射内置模块
'''
# import time
# print(time.time())
# t=getattr(time,'time')
# print(t())

# --------------------------------------------------------
# 作业题
# 魔术方法 __eq__ 方法练习
# class Myint(int):
#     def __eq__(self, other):
#         # 自定义规则:如果2个数都能被6整除则相等，其余都不相等
#         if self%6==0 and other%6==0:
#             return True
#         else:
#             return False
# no1=Myint(6)
# no2=Myint(12)
# result=no1==no2
# print(result)

# 魔术方法 __hash__ 和 __eq__练习

# 设计二维坐标类Point，比较2个坐标是否相等？
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __hash__(self):
        return hash((self.x,self.y))
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
p1=Point(1,2)
p2=Point(1,2)
print(hash(p1))
print(hash(p2))
print(p1 is p2)
print(p1 == p2)









