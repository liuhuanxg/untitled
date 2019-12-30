# a=3
# b=[]
# def fun(a,b):
#     a+=3
#     b.append(3)
# fun(a,b)
# print(a)
# print(b)

'''
注意，易混
'''
# 不可变参数类型
# def hs(a):
#     a+=3
# a=5
# print(a)

# 全局 局部
# a=5
# def hs():
#     a+=3    # 报错 local variable 'a' referenced before assignment
# hs()
# print(a)

# a=3
# b=4
# c=5
# def out():
#     a=30
#     b=40
#     def inside():
#         a=300
#         print(a)
#         print(b)
#         print(c)
#         print(__name__)
#     inside()
# out()

'''
global和nonlocal关键字的作用
'''

'''
globles()--访问全局命名空间
locals()--访问局部命名空间
返回值类型：字典
'''