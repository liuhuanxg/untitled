'''
全局变量是不可变数据类型，函数无法修改全局变量的值
全局变量是可变数据类型，函数可以修改全局变量的值
'''
# 此时外部的a，与内部的a没有任何关系
# a=10
# b=[]
# def x():
#     a=8
#     b.append(9)
#     print(a)
# x()
# print(a)
# print(b)

# 此时外部的b，与内部的b没有任何关系
# b=[]
# def x():
#     b=[9]
#     print(b)
# x()
# print(b)

# b=[]
# def x():
#     b.append(9)
# x()
# print(b)