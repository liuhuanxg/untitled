# 补充知识点

'''
逻辑运算符：and/or/not
'''
# stu=True
# if not stu:
#     print('你不是学生')
# else:
#     print('是学生，可以进学校')

'''
短路逻辑
x or y
如果x为False，返回y的值
如果x为True，返回True
'''
# a=5
# b=a>7 or 4
# print(b)    # 4
# a=5
# b=a>3 or 7
# print(b)    # True

'''
短路逻辑
x and y
如果x为False，返回False
如果x为True，返回y的值
'''
a=6
b=a>7 and 5
print(b)

'''
三元表达式
满足if条件，值为前面的值
不满足则为后面的值
'''
b=11
a=7 if b>10 else 8
print(a)

b=9
a=7 if b>10 else 8
print(a)

'''
while/for...else...
'''
# i=1
# while i<5:
#     if i==4:
#         break
#     print(i)
#     i+=1
# else:
#     print('好像不成立了')

# 质数
# n=int(input('请输入一个数：'))
# i=2
# while i<n//2:
#     if n%i==0:
#         print(n,'不是质数')
#         break
#     i+=1
# else:
#     print(n,'是质数')

# n=int(input('请输入一个数：'))
# for i in range(2,(n//2)+1):
#     if n%i==0:
#         print(n,'不是质数')
#         break
# else:
#     print(n,'是质数')

# 2--100质数放入列表
# s=[]
# for n in range(2,101):
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             break
#     else:
#         s.append(n)
# print(s)

# a=[]
# i=2
# while i<100:
#     j=2
#     while j<i:
#         if i%j==0:
#             break
#         j+=1
#     else:
#         a.append(i)
#     i+=1
# print(a)