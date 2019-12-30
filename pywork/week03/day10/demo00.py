class A():
    n=100
    lst=[1,2]
a=A()
a.n=3
print(a.n)    # 3
print(A.n)    # 100
delattr(a,'n')
print(a.n)    # 100

b=A()
b.lst.append(5)
print(A.lst)    # [1,2,5]
print(b.lst)    # [1,2,5]
# A.lst=[100]
# print(a.lst)    # [100]
# print(A.lst)    # [100]
a.lst=100
print(A.lst)
print(a.lst)