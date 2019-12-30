#Python 0715  吕佳

# a=True+3
# print(a)
# b=False*3
# print(b)
#
# x=2
# y=3.4
# z=x+y
# print(z,type(z))
# z=int(z)
# print(z,type(z))
# z=float(z)
# print(z,type(z))

#不可逆
# a=3
# b=bool(a)
# print(b)
# c=int(b)
# print(c)
#
# x=input("请输入：")
# print(x,type(x))
# y=int(x)
# print(y,type(y))

# price=input('请输入西红柿单价：')
# a=int(price)
# print(a,type(a))

#解决
# price=input('请输入西红柿单价：')
# a=float(price)
# b=int(a)
# print(b,type(b))
#
# x=int(float(input("请输入人数：")))
# print(x,type(x))

#十进制->其他进制
#注：使用函数进制转换后，结果皆为字符串类型
# a=120
# b=hex(a)          #十六进制
# print(b,type(b))
#
# a=hex(0o42)       #八进制转十六进制
# print(a,type(a))
#
# a=119
# b=oct(a)          #八进制
# print(b,type(b))
#
# a=12
# b=bin(a)          #二进制
# print(b,type(b))

#其他进制->十进制
# a=int('11',8)
# print(a)
#
# print(int('11',16))
#
# print(int('11',2))
#
# print(int('AB',16))
#
# print(int('3F',16))
#
# print(int('11001',2))

# a=input("请输入一个是十六进制数：")
# b=int(a,16)
# print("转换为十进制为：",b)
#
#
# x=input("请输入一个八进制数：")
# y=int(x,8)
# print("转换为十进制为：",y)

# m=input("请输入一个二进制数：")
# n=int(m,2)
# print("转换为十进制为：",n)

#改变引用
# a=15
# print(type(a))
# a='tom'
# print(type(a))
#
# a=10
# b=a
# print(a==b)
# print(a is b)

# a=10
# b=a
# a=5
# print(b)

# a=3
# b=4
# c=a+b
# print(c)
#
# #字符串拼接
# a='3'
# b='4'
# c=a+b
# print(c)
#
# #重复
# a='abc'
# b=a*3
# print(b)

#python关键字列表
# import keyword
# print(keyword.kwlist)

#chr()函数  将一个整数转换为一个字符   ASCII
# a=int(input('请输入一个整数：'))
# print(chr(a))

#输入一个大写字母，判断这个大写字母是字母表中的第几个
# a=input("请输入一个大写字母：")
# print(ord(a)-65+1)  #ord函数--参数为字符，返回值为它对应的ASCII码

# '//'向下取整，丢弃小数部分   两个运算数有小数，结果就是小数
# a=-9.5
# b=3
# c=a//b
# print(c)

# a=9.5
# b=3
# c=a//b
# print(c)

# '**'幂
# a=5
# print(a**2)
# print(a**3)

# '%'取余
# a=5//3
# print(a)
#
# b=5%3
# print(b)

#数字倒置
# a=123
# x=a//100   #百
# y=a//10%10 #十
# z=a%10     #个
# b=z*100+y*10+x
# print(b)

# a=int(input("请输入一个三位数："))
# x=a%10    #个
# y=a//10%10#十
# z=a//100  #百
# print(x*100+y*10+z)

#循环
# x=int(input("请输入一个数："))
# y=0
# while x!=0:
#     y=y*10+x%10
#     x=x//10
# print(y)

#求50以内的偶数
# a=1
# while a<50:
#     if a%2==0:
#         print(a)
#     a+=1

#砍价--砍去小数和个位数
# price=float(input('请输入西红柿单价：'))
# num=float(input('请输入斤数：'))
# # money=int(price*num)//10*10
# # print(money)
# money=int(price*num)
# money=money-money%10
# print(money)

# a=4
# a+=5
# print(a)
# a-=5
# print(a)
# a*=2
# print(a)
# a/=2
# print(a)
# a%=5
# print(a)
# a//=2
# print(a)
# a**=3
# print(a)

#str()函数
# a=4
# b=str(a)
# print(b,type(b))
#
# a=4.5
# b=str(a)
# print(b,type(b))

#eval(str)函数   用来计算在字符串中的有效 python 表达式,并返回一个对象
# a='1+2'
# print(a)
# b=eval(a)
# print(b)

#------------------------------------------------------
# a=10
# b=a
# a=5
# print(b)

# a=3
# b=4
# c=a+b
# print(c)
#
# a='3'
# b='4'
# c=a+b
# print(c)

# a='abc'
# b=a*3
# print(b)

# import keyword
# print(keyword.kwlist)

# a=int(input("请输入一个整数："))
# print(chr(a))
#
# a=input('请输入一个大写字母：')
# print(ord(a)-65+1)

# a=-9.5
# b=3
# c=a//b
# print(c)
#
# a=9.5
# b=3
# c=a//b
# print(c)

# a=5
# print(a**2)
# print(a**3)

#数字倒置
# a=int(input('请输入一个三位数：'))
# x=a%10
# y=a//10%10
# z=a//100
# print(x*100+y*10+z)

#循环
# x=int(input("请输入："))
# y=0
# while x!=0:
#     y=y*10+x%10
#     x//=10
# print(y)

#50以内偶数
# a=1
# while a<50:
#     if a%2==0:
#         print(a)
#     a+=1

# price=float(input('请输入西红柿单价：'))
# num=float(input("请输入数量："))
# money=int(price*num)
# money=money-money%10
# print(money)

# a=4.5
# b=str(a)
# print(b,type(b))

# a='1+2'
# print(a)
# b=eval(a)
# print(b)
#------------------------------------------------------
# 作业题
# 类型转换题
# # 1.计算 True+100的值
# print(True+100)      #101
# # 2.将3.14 转换成 整数和布尔值
# print(int(3.14))      #3
# print(bool(3.14))     #True
# # 3.将十进制20分别使用二进制、八进制、十六进制进行转换
# print(bin(20))     #0b10100
# print(oct(20))     #0o24
# print(hex(20))     #0x14
# # 4.将字符串‘123’转换为int类型的数值，赋值给num,并查看num数据类型
# num=int('123')
# print(num,type(num))
# # 5.计算2的10次方
# print(2**10)      #1024
# # 6.计算出101除以3的余数
# print(101%3)      #2
# # 7.将 65 转换成 A
# print(chr(65))
# # 8.计算 字符串 "10/2" 的值
# print(eval('10/2'))
# # 9.超市买苹果
# # 收银员向机器输入苹果的单价，输入客户购买的数量，显示总价格
# price=float(input("请输入苹果单价："))
# num=float(input("请输入购买数量："))
# print('总价格为：',price*num)
# # 10. 数字逆序输出
# a=int(input("请输入一个三位数："))
# x=a//100
# y=a//10%10
# z=a%10
# b=x+y*10+z*100
# print(b)