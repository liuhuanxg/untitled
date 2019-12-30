'''
方法的重写
'''
class A():
    def hehe(self):
        print('A:呵呵')
class B(A):
    def hehe(self):
        print('B:呵呵')
a=A()
b=B()
a.hehe()
b.hehe()