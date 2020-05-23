"""
类变量：是可在类的所有实例之间共享的值（也就是说不是单独分配给每个实例），如下：

实例变量：实例化之后，每个实例单独拥有的变量

"""
"""
class Test(object):
    num=0
    def __init__(self,name):
        self.name=name
        Test.num += 1
"""

class Test(object):
    age = 1
    __slots__ = ["name","num"]
    def __init__(self,name):
        self.name = name
        Test.age += 1

if __name__=="__main__":
    # print(Test.num)
    t1=Test('jack')
    # print(Test.num)
    t2=Test('lucy')
    # print(t1.name,t1.num)
    # print(t2.name,t2.num)
    Test.class_str="添加类变量"
    print(Test.class_str)
    print(t1.class_str)
    print(t2.class_str)
    t1.age = 20
    print(Test.age)