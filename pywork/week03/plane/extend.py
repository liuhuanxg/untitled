num=int(input('请输入一个十进制数：'))
lst=[]
while num!=0:
    a=num%16
    if 0<=a<=9:
        lst.append(a)
    elif 10<=a<=15:
        lst.append(chr(97+a-10))
    else:
        print('数据有误')
    num//=16
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end='')