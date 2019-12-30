#改变引用
a=15
print(type(a))
a='tom'
print(type(a))

a=10
b=a
print(a==b)
print(a is b)

a=10
b=a
a=5
print(b)