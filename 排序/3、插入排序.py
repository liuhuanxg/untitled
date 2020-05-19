#工作原理：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。时间复杂度On2。

#时间复杂度平均O(n2)，最好为O(n),最坏为O(n2),空间复杂度为O(1)，稳定排序

list1=[2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]

# 一、直接插入排序
def insert_sort(alist):
    #从第二个位置，即下标为1的元素开始向前插入
    for i in range(1,len(alist)):
        #第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break
        print(alist)
insert_sort(list1)




# 二、折半插入排序
"""
list2 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序

list3 = [list2[0]]
del list2[0]

for i in list2:
    index_now = [0, len(list3)]
    print("list3:", list3, "index_now:", index_now)
    while 1:
        index = index_now[0] + int((index_now[1]-index_now[0])/2)
        print("index1",index, (index_now[1]-index_now[0]))
        if i == list3[index]:
            list3.insert(index+1, i)
            break
        #如果更新的index值在index_now中存在(也有可能是边界),就表明无法继续更新
        elif index in index_now:
            list3.insert(index+1,i)
            break
        elif i>list3[index]:
            index_now[0] = index
        elif i<list3[index]:
            index_now[1] = index
print(list3)

"""
