# def hs():
#     b=3
#     print(a)
#     print(b)
# a=6
# hs()
# print(b)    # 报错 name 'b' is not defined

# 局部变量与全局变量同名，函数内以局部变量为准
# def hs():
#     a=7
#     print(a)    # 7
# a=9
# hs()
# print(a)    # 9

# 全局变量和局部变量，不可共存
# 局部变量有，不去外面找
# def hs():
#     # print(a)    # 报错 local variable 'a' referenced before assignment
#     a=9
#     print(a)
# a=10
# hs()
# print(a)

# 原因同上
# def hs():
#     a+=3    # 报错 local variable 'a' referenced before assignment
#     print(a)
# a=10
# hs()