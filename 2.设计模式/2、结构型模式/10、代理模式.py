#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 10、代理模式.py
@Time: 2020/5/16 21:58
@user：liuhuan   
"""
"""
当我们想要把一个计算成本较高的对象的创建过程延迟到用户首次真正使用它的时候才进行创建。

这类操作通常使用代理设计模式(Proxy design pattern)来实现。该模式因为使用代理对象在访问实际对象之前执行重要操作而得其名。

比较知名的代理有四种类型：
    ·远程代理：实际存在于不同地址空间(例如，某个网络服务器)的对象在本地的代理者。
    ·虚拟代理：用于濑初始化，将一个大计算量对象的创建延迟到真正需要的时候进行。
    ·保护/防护代理：控制对敏感对象的访问。
    ·智能(引用)代理：在对象被访问时执行额外的动作。此类代理的例子包括引用计数和线程安全检查。
    

在面向对象编程[OOP(Object Oriented Programming)]，有两种基本的、不同类型的濑初始化，如下：
    ·在实例级：意味着会对一个对象的特性进行濑初识化，但该特性有一个对象作用域。同一个类的每个实例(对象)都有自己的(不同的)特性副本。
    ·在类级或模块级：在这种情况下，我们不希望每个实例都有一个不同的特性的副本，而是所有的实例同享同一个特性，而特性是濑初始化的。


代理的应用案例：
    1、在使用私有网络或云搭建一个分布式系统时。在分布式系统中，一些对象存在于本地内
存中，一些对象存在于远程计算机的内存中。如果我们不想本地代码关心两者之间的区
别，那么可以创建一个远程代理来隐藏/封装，使得应用的分布式性质透明化。
    2、因过早创建计算成本较高的对象导致应用遭受性能问题之时。使用虚拟代理引入懒初始化，仅在真正需要对象之时才创建，能够明显提高性能。
    3、用于检查一个用户是否有足够权限来访问某个信息片段。如果应用要处理敏感信息（例如，医疗数据），我们会希望确保用户在被准许之后才能访问/修改数据。一个保护/防护代理可以处理所有安全相关的行为。
    4、应用（或库、工具集、框架等）使用多线程，而我们希望把线程安全的重任从客户端代码转移到应用。这种情况下，可以创建一个智能代理，对客户端隐藏线程安全的复杂性。
    5、对象关系映射（Object-Relational Mapping，ORM）API也是一个如何使用远程代理的例子。包括Django在内的许多流行Web框架使用一个ORM来提供类OOP的关系型数据库访问。ORM是关系型数据库的代理，数据库可以部署在任意地方，本地或远程服务器都可以。
    
"""

"""
# 1、简单的代理使用
class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        # print('function overriden: {}'.format(self.fget))
        # print("function's name: {}".format(self.func_name))
    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value

class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None
    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5)) # 假设这一行的计算成本比较大
        return self._resource

def main():
    t = Test()
    print(t.x)
    print(t.y)
    print(t.resource)
    print(t.resource)

if __name__ == '__main__':
    main()
"""


# 2、完整代理模式
"""
示例：设置保护代理实现查看用户和添加用户
    ·查看用户列表：这一操作不需要特殊权限
    ·添加新用户：这一操作要求客户端提供一个特殊的密码
"""

class SensitiveInfo():
    def __init__(self):
        self.users = ["nick", "tom", "ben", "mike"]

    def read(self):
        print("有{}个用户：{}".format(len(self.users)," ".join(self.users)))

    def add(self, user):
        self.users.append(user)
        print("添加用户{}".format(user))



class Info:
    """SensitiveInfo的保护代理"""
    def __init__(self):
        self.proteced = SensitiveInfo()
        self.secret = "root"

    def read(self):
        self.proteced.read()

    def add(self,user):
        sec = input("请输入密码：")
        if self.secret == sec:
            self.proteced.add(user)
        else:
            print("密码错误！")

def main():
    info = Info()
    while True:
        print("""1：查看用户
2：添加用户
3：quit""")
        key = input("请输入选项：")
        if key == "1":
            info.read()
        elif key== "2":
            name = input("请输入用户名：")
            info.add(name)
        elif key == "3":
            exit()
        else:
            print("选项有误，请重新选择！")

if __name__ == "__main__":
    main()