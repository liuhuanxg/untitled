timeStr=input("输入时间")
list=timeStr.split(':')
# print(list)
h=int(list[0])
m=int(list[1])
s=int(list[2])
s+=1
if s>=60:
    m+=1
    s=0
    if m>=60:
        h+=1
        m=0
        if h==24:
            h=0
print('%d:%d:%d'%(h,m,s))