# 只要继承object类就是新式类
# 不继承object类的都是经典类

"""
在python3 所有的类都继承object类，都是新式类
在python2中，不继承object的类都是经典类
            继承object的类就是新式类了
在py2中
class A:pass            经典类
class B(object):pass    新式类

在py3中：
class A():pass          新式类
class B():pass          新式类

经典类的多继承深度优先
新式类的多继承广度优先
"""

"""
# 一、简单继承
class A():
    def run(self):
        print("A类 执行")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

print(D.mro())  #DBCA

"""


"""
# 2、复杂继承
class A():
    def run(self):
        print("A类 执行")

class B(A):
    pass

class C(B):
    pass

class D(C):
    pass

class E(B):
    pass

class F(D,E):
    pass

print(F.mro())  #FDCEBA
"""


"""
#3、复杂多继承
class A():
    def run(self):
        print("A类 执行")

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C):
    pass

class F(D,E):
    pass

print(F.mro())  #FDCEBA

"""

"""
# C3算法详解
F(D,E)=mergo(D(B),E(C))
    =[F] +[DBAO] +[ECAO]
    FDB = [AO]+[ECAO]
    FDBEC = [AO]+[AO]
    FDBECA = [O]
    FDBECAO
"""

# 案例练习
class A():
    def run(self):
        print("A类 执行")

class B(A):
    pass

class C():
    pass

class D(B):
    pass

class E(C):
    pass

class F(D,E):
    pass

print(F.mro())

"""
F+DBAO+ECO
FDBAECO
"""