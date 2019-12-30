'''
检测一个类，是否为另一个类的子类
issubclass(被检测类，父类)，若一次判断多个父类，有一则为真
isinstance(对象，类)，若一次判断多个类，有一则为真
'''
class A():
    pass
class B(A):
    pass
print(issubclass(B,A))
a=A()
print(isinstance(a,A))