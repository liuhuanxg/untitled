a=4
a+=5
print(a)    #9
a-=5
print(a)    #4
a*=2
print(a)    #8
a/=2
print(a)    #4.0
a%=5
print(a)    #4.0
a//=2
print(a)    #2.0
a**=3
print(a)    #8.0

#str()函数
a=4
b=str(a)
print(b,type(b))

a=4.5
b=str(a)
print(b,type(b))

#eval(str)函数   用来计算在字符串中的有效 python 表达式,并返回一个对象
a='1+2'
print(a)
b=eval(a)
print(b)
