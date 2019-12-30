'''
函数：
def 函数名():
    代码段
组织好的，可重复使用的，用来实现独立功能的代码段。
可以提高程序的代码重用率。
'''
def prt(f):    # 定义函数
    print('西单大悦城',f,'层欢迎您')
    print('1楼、鞋类商品')
    print('2楼、女性服饰')
    print('3楼、男装')
    print('您现在在',f,'层')
floor=int(input('请输入楼层：'))
if floor==1:
    prt(1)    # 调用函数
elif floor==2:
    prt(2)
elif floor==3:
    prt(3)