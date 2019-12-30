# 同
a=[1,2,3]
b=a
a.append(4)
print(a,id(a))
print(b,id(b))
# 不同
a=[1,2,3]
b=[1,2,3]
print(a,id(a))
print(b,id(b))
# 不同
a=3
b=a
a=5
print(a,id(a))
print(b,id(b))
# 同
a='abc'
b='abc'
print(a,id(a))
print(b,id(b))