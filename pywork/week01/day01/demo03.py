#不可逆
a=3
b=bool(a)
print(b)
c=int(b)
print(c)

#凡是用input输入的数据，皆为字符串
x = input("请输入")
print(x, type(x))
y = int(x)
print(y, type(y))