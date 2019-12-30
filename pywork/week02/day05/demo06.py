'''
返回值
没有return的函数，均返回空值None
python中可以返回多个值--元组类型
return的两个作用：1.返回内容 2.结束此方法
'''
# def qiuhe(a,b):
#     c=a+b
#     return c
# x=qiuhe(1,2)
# print(x)
# y=qiuhe(10,20)
# print(y)

# a=[1,2,30,]
# x=a.remove(30)
# #!!!a=[1,2]，x=None，说明remove()是一个有参数没有返回值的函数
# print(x)    # None

# 返回值为多个值
# def hs(a,b):
#     c=a+b
#     d=a-b
#     e=a*b
#     return c,d,e
# # x=hs(5,6)
# # print(x)    # (11, -1, 30)
# x,y,z=hs(5,6)
# print(x,y,z)    # 11 -1 30

# def hanshu(a,b):
#     return
#     c=a+b
#     d=a-b
#     return c,d
# x=hanshu(5,6)
# print(x)

def hs():
    i=0
    while i<5:
        if i==2:
            return
        print(i)
        i+=1
x=hs()
print(x)