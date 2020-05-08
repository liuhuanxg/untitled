"""
类变量：是可在类的所有实例之间共享的值（也就是说不是单独分配给每个实例），如下：

实例变量：实例化之后，每个实例单独拥有的变量

"""
class Test(object):
    num=0
    def __init__(self,name):
        self.name=name
        Test.num += 1
if __name__=="__main__":
    print(Test.num)
    t1=Test('jack')
    print(Test.num)
    t2=Test('lucy')
    print(t1.name,t1.num)
    print(t2.name,t2.num)