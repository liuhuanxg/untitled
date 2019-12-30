# 函数嵌套 enclosing
# 原理同局部变量
# def outside():
#     def inside():
#         print('我是内部')
#     inside()
#     print('我是外部')
# outside()
# # inside()

# def out():
#     a=9
#     def inside():
#         a=98
#         print('我是内部',a)
#     inside()
#     print('我是外部',a)
# out()

# nonlocal关键字可以修改外层（非全局）变量
# def out():
#     a=9
#     def inside():
#         nonlocal a
#         a=98
#         print('我是内部',a)
#     inside()
#     print('我是外部',a)
# out()

# a=9
# def out():
#     def inside():
#         nonlocal a
#         a=98
#         print(a)
#     inside()
# out()

# a=9
# def out():
#     a=7
#     def inside():
#         nonlocal a
#         a=999
#         print(a)
#     inside()
#     print('-------------',a)
# out()
# print(a)