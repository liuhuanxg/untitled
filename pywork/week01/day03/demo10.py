# 赋值、浅拷贝、深拷贝
import copy
a=[1,2,3,[4,5,[10,20]],6]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))

a.append(7)
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))

a[3].append(99)
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))

a[3][2].append(30)
print(a,id(a))
print(b,id(b))
print(c,id(c))
print(d,id(d))