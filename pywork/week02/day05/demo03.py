'''
参数的定义方式：
1.位置参数
2.关键字参数
!!!关键字参数和位置参数同时使用时，调用时关键字参数必须是在位置参数后面的
3.默认参数
!!!默认参数只能放在后面的
4.可变参数(*a,**a)
'''
# 关键字参数
# 无视参数顺序
# def cha(a,b):    # a:3 b:1
#     print(a-b)
# cha(b=1,a=3)

# def hs(a,b,c):
#     print(a,b,c)
# hs(2,3,c=7)
# 关键字参数和位置参数同时使用时，关键字参数必须在位置参数后面定义
# hs(a=2,4,5)    # 报错

# 默认参数
# def dengji(name,age,sex='男'):
#     print(name,age,sex)
# dengji('张三',19)
# dengji('李四',20,'男')
# dengji('王五',21,'女')

# def xiaozhu(a=3,b):     # 报错
# def xiaozhu(b,a=3):
#     print(a,b)
# xiaozhu(1,2)