data=input('请输入一个字符串：')
h=1
j=0
for i in range(len(data)):
    print(data[i],end='')
    j+=1
    if j==h:
        print()
        j=0
        h+=1