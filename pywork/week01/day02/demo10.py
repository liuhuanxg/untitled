'''
输入十个数
如果输入的<18,不参加运算
如果输入的>65，跳出循环
求输入的年龄的平均值
'''
i=1
n=0
sum=0
while i<=10:
    age=int(input('请输入年龄：'))
    if age<18:
        i+=1
        continue
    elif age>65:
        break
    else:
        sum+=age
        i+=1
        n+=1
if n==0:
    print('无有效数据！')
else:
    print("平均值为：",(sum//n))