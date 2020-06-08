#-*-coding:utf-8 -*-
"""
@project:untitled
@File: day1.py
@Time: 2020/6/6 13:50
@user：liuhuan   
"""
# 单行注释
number1 = 100
number2 = 200.01
bool1 = True
str1 = "hello"
print(type(number1))    # int
print(type(number2))	# float
print(type(bool1))	    # bool
print(type(str1))	    # str

str2 = "11.2"
print(float(str2))

"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author: youzi
"""
a =  int(3.4)
b = int(3.5)
c = int("12")
print(a,b,c)

for i in range(5):
    print(i)
    break
else:
    print("else")


