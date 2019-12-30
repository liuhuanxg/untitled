'''
'%'号取余
'''
a=5//3
print(a)

b=5%3
print(b)

#倒置
a=123
x=a%10
y=int(a/10)%10
z=int(a/100)
b=x*100+y*10+z
print(b)

a = int(input('请输入一个三位数：'))
x = a % 10
y = a // 10 % 10
z = a // 100
b = x * 100 + y * 10 + z
print(b)
