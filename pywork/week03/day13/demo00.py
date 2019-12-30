'''
实例方法、类方法、静态方法
及其调用
'''
class A():
    def f1(self,x):
        self.x=x
    @classmethod
    def f2(cls):
        print('哈哈')
    @staticmethod
    def f3(a,b):
        return a+b
a=A()
a.f1(1)
print(a.x)
A.f2()
a.f2()
print(a.f3(1,3))
print(A.f3(1,3))