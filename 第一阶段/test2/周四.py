class A():
    def text(self):
        print('我是a里边的函数')
class B():
    def text(self):
        print('我是b里边的函数')
class C(B,A):
    pass
c=C()
c.text()