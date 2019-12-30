# global关键字可以将局部变量变成一个全局变量

# def hs():
#     global a
#     a+=10
#     print('函数内部：%d' % a)    # 30
# a=20
# hs()
# print('函数外部：%d' % a)    # 30

# def hs():
#     global a
#     a=10
# hs()
# print(a)

# def hs():
#     global a
#     a=10
# print(a)    # 报错 name 'a' is not defined
# hs()
# print(a)