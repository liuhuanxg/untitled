'''
不可变类型的参数：数字、字符串、元组
函数hs(a)内部修改a的值，只是修改了一个副本，不会对a本身造成影响
可变类型的参数：列表、字典、集合
fun(la)将la真正的传过去，修改后fun外部的la也会受影响
'''
# 不可变
# def hs(a):
#     a+=3
#     print('函数内部a=',a)
# x=10
# hs(x)
# print('函数外部x=',x)

# 可变
# def hs(a):
#     a.append(3)
#     print(a)
# x=[1,2]
# hs(x)
# print(x)

# def hs(a):
#     a['age']=19
#     print(a)
# x={'name':'张三'}
# hs(x)
# print(x)

# 默认参数如果是可更改类型，程序运行时会有逻辑错误
# 逻辑错误
# def hs(a=[]):
#     a.append(10)
#     print(a)
# hs()    # [10]
# hs()    # [10,10]

# 实参走后对形参没有任何影响，除非再来
# def hs(a=[]):
#     a.append(10)
#     print(a)
# hs()    # [10]
# b=[9]
# hs(b)    # [9,10]
# hs()    # [10,10]
# hs(b)    # [9,10,10]
# hs([])
# hs([])

# !!!这不叫修改
def hs(a):
    a=[1,2]    # 重新赋值
    print(a)
b=[3,4]
hs(b)
print(b)