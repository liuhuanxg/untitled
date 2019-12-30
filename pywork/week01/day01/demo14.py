#砍价--抹去小数和个位  1
# price=float(input("请输入西红柿单价："))
# num=float(input('请输入斤数：'))
# m=int(price*num)//10*10      #int()--去掉小数   //10*10--去掉个位
# print(m)

#  2
price=float(input("请输入西红柿单价："))
num=float(input('请输入斤数：'))
money=int(price*num)
money=money-money%10
print(money)