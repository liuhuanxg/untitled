# 1、写一个函数实现斐波那契数列(1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233，377......)
# 要求：接收一个参数，返回一个存着等量值的列表
lst=[]
def func(num):
    a=1
    b=1
    for i in range(1,num+1):
        if i==1 or i==2:
            lst.append(1)
        else:
            a,b=b,a+b
            lst.append(b)
func(6)
print(lst)