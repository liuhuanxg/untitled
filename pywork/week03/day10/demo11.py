'''
多继承
'''
# class A():
#     def t(self):
#         print('A:t1')
# class B():
#     def t(self):
#         print('B:t2')
# class C(A,B):
#     def t(self):
#         print('C:t3')
# c=C()
# c.t()

# class A():
#     def tx(self):
#         print('A:t1')
# class B():
#     def tx(self):
#         print('B:t2')
# class C(A,B):
#     def t(self):
#         print('C:t3')
# c=C()
# c.tx()

class A():
    def tx(self):
        print('A:t1')
class B():
    def tx(self):
        print('B:t2')
class C(B,A):
    def t(self):
        print('C:t3')
c=C()
c.tx()