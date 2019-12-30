'''
反射方法
hasattr()--判断是否有此变量，返回值为bool类型
getattr()--获取属性值或者获取方法变量的地址，返回值为值
delattr()--删除类或者对象的属性或方法
setattr()--给类或者对象设置属性或者方法
'''
# class A():
#     dog=0
#     def hehe(num):
#         print(num)
# setattr(A,'dog',90)
# print(A.__dict__)
# setattr(A,'cat',10)
# print(A.__dict__)
#
# a=A()
# print(a.__dict__)
# setattr(a,'haha',1999)
# print(a.__dict__)
# a.hehe=2022
# print(a.__dict__)
#
# print(getattr(A,'dog'))
# f=getattr(A,'hehe')
# f(1)
# delattr(A,'dog')
# print(hasattr(A,'dog'))


class A():
    def f1(self):
        print('我是f1')
    def f2(self):
        print('我是f2')
    def f3(self):
        print('我是f3')
print(A.__dict__)
a=A()
while True:
    f=input('请输入你想调用的方法：')
    if hasattr(A,f):
        fc=A.__dict__.get(f)
        fc(a)
    else:
        print('A类没有',f)