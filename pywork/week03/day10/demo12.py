# class A():
#     def func(self):
#         print('A开始')
#         print('A结束')
# class B(A):
#     def func(self):
#         print('B开始')
#         super().func()
#         print('B结束')
# class C(A):
#     def func(self):
#         print('C开始')
#         super().func()
#         print('C结束')
# class D(B,C):
#     def func(self):
#         print('D开始')
#         super().func()
#         print('D结束')
# print(D.mro())
# d=D()
# d.func()

# class A():
#     def __init__(self):
#         print('A开始')
#         print('A结束')
# class B(A):
#     def __init__(self):
#         print('B开始')
#         super().__init__()
#         print('B结束')
# class C(A):
#     def __init__(self):
#         print('C开始')
#         super().__init__()
#         print('C结束')
# class D(B,C):
#     def __init__(self):
#         print('D开始')
#         super().__init__()
#         print('D结束')
# print(D.mro())
# d=D()

class A():
    def __init__(self):
        print('A')
        super().__init__()
class B():
    def __init__(self):
        print('B')
        super().__init__()
class C(A,B):
    def __init__(self):
        print('C')
        super().__init__()
c=C()
print(C.mro())