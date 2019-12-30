#遍历二维列表
a=[[1,2,3],[4,5,6,7],[8,9],10]
for x in a:
    if type(x)!=list:
        print(x)
    else:
        for y in x:
            print(y,end=' ')
        print()

# 输出3 6 9
print(a[0][2])
print(a[1][2])
print(a[2][1])