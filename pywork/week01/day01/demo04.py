'''
输入的为整型，运行成功
输入的为浮点型，则提示出错
'''
price=input('请输入西红柿单价：')
a=int(price)
print(a,type(a))

#解决
price=input('请输入西红柿单价：')
a=float(price)
b=int(a)
print(b,type(b))

x=int(float(input('请输入人数：')))
print(x,type(x))




