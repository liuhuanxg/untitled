# class A():
#     pass
# A.x=99
# print(A.x)
# a=A()
# print(a.x)
# print(id(a.x))
# print(id(A.x))

# class A():
#     def __new__(cls, *args, **kwargs):
#         cls.xIns=object.__new__(cls)
#         return cls.xIns
#     def __init__(self,name):
#         self.name=name
# zs=A('张三')
# print(zs.name)
# print(A.xIns.name)
# ls=A('李四')
# print(A.xIns.name)
# print(zs is ls)

'''
单例模式
'''
# class A():
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'xIns'):
#             cls.xIns=object.__new__(cls)    # 产生一个此类的对象
#         return cls.xIns
#     def __init__(self,name):
#         self.name=name
# zs=A('张三')
# print(A.xIns.name)
# ls=A('李四')
# print(A.xIns.name)
# print(zs.name)
# print(zs is ls)