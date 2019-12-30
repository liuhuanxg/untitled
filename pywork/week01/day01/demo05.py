#10进制->其他进制
#使用函数进制转换后，结果皆为字符串类型
a=120
b=hex(a)           #十六进制
print(b,type(b))

a=hex(0o42)        #十六进制        0o42--八进制
print(a,type(a))

a=119
b=oct(a)           #八进制
print(b,type(b))

a=12
b=bin(a)           #二进制
print(b,type(b))

#其他进制->10进制
a=int('11',8)
print(a)

b=int('11',16)
print(b)

c=int('11',2)
print(c)

a=int('AB',16)
print(a)

b=int('3F',16)
print(b)

c=int('11001',2)
print(c)