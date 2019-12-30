#任何位数，数字倒序
num=int(input('请输入一个数字：'))
y=0
while num!=0:
    y=y*10+num%10
    num//=10
print(y)