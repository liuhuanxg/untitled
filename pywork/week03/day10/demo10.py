class A():
    num=3
    __num1=2
    def __init__(self,x,y):
        self.x=x
        self.y=y
class B(A):
    num=10    # 静态属性、类属性
    def __init__(self,x,y,z):
        self.z=z
        super().__init__(x,y)
b=B(1,2,3)
print(b.x)
print(B.num)
# print(B.__num1)    # 报错
print(A.num)

# super()还可以从外部使用，需要传递类名（本类）和对象名
print(super(B,b).num)