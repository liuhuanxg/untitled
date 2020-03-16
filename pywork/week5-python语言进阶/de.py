# 冒泡排序特点：第一次排序之后最大的数一定在最后。
list1=[4,5,9,3,6]
for i in range(1,len(list1)):
    for j in range(len(list1)-i):
        if list1[j]>list1[j+1]:
            list1[j+1],list1[j]=list1[j],list1[j+1]
print(list1)


