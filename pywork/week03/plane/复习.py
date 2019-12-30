# a=[]
# if not a:
#     print(2)
# else:
#     print(3)
#
# b=''
# if not b:
#     print('2a')
# else:
#     print('2c')

# def hs(a):
#     a+=5
# a=7
# hs(a)
# print(a)

# 报错
# def hs():
#     a+=5
# a=7
# hs(a)
# print(a)

# 多态
# class Dog():
#     def jiao(self):
#         print('汪汪')
# class Cat():
#     def jiao(self):
#         print('喵喵')
# def jiao(a):
#     a.jiao()
# d=Dog()
# c=Cat()
# jiao(d)
# jiao(c)

# 钻石继承
# class A():
#     def __init__(self):
#         print('A开始')
#         print('A结束')
# class B(A):
#     def __init__(self):
#         print('B开始')
#         super(B, self).__init__()
#         print('B结束')
# class C(A):
#     def __init__(self):
#         print('C开始')
#         super(C, self).__init__()
#         print('C结束')
# class D(B,C):
#     def __init__(self):
#         print('D开始')
#         super().__init__()
#         print('D结束')
# d=D()

# 单例
# class D():
#     xIns=None
#     def __new__(cls, *args, **kwargs):
#         if not cls.xIns:
#             cls.xIns=object.__new__(cls)
#         return cls.xIns
#     def __init__(self,name):
#         self.name=name
# zs=D('张三')
# ls=D('李四')
# print(zs.name)
# print(zs is ls)

# while True:
#     try:
#         a=int(input('请输入一个数：'))
#     except TypeError as f:
#         print(f,'类型错误')
#     except ValueError as f:
#         print(f,'值错误')
#     else:
#         print('没有错误')
#     finally:
#         print('错误与否都执行')

# def func(num1,*num2,num3=10):
#     return num1*num3
# print(func(2,1,3))

# with open('a.txt','r') as f:
#     # tell()--当前游标位置
#     print(f.tell())
#     a=f.read(3)
#     print(f.tell())
#     a=f.read(5)
#     print(f.tell())
#     # seek()--重新设置当前游标位置
#     # 第一个参数--位移个数
#     # 第二个参数--从哪个位置位移
#     f.seek(3,0)
#     print(f.read())