'''
函数：
只在调用的时候执行
函数必须先定义后调用
参数--argument：
定义的时候，称为形参，因为没有实际的值
调用时，你给它什么值，它就是什么值
'''
# def qiuhe2(a,b):
#     c=a+b
#     print(c)
# qiuhe2(2,3)
# qiuhe2(5,6)

# 函数调用的本质是函数名对应的内存地址
# def qiuhe3(a,b,c):
#     s=a+b+c
#     print(s)
# qiuhe3(1,2,3)
# print(qiuhe3)    # <function qiuhe3 at 0x000000000209D1E0>
# qiuhe=qiuhe3    # 将qiuhe3的内存地址赋给qiuhe变量
# # 同
# print(id(qiuhe3))
# print(id(qiuhe))
# qiuhe(1,2,3)

# def hs():
#     print(i+1)
# i=5
# a=hs
# b=hs
# a()    # 6
# i=7
# a()    # 8
# b()    # 8