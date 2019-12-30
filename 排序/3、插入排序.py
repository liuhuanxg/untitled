#工作原理：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在是线上，再从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。时间复杂度On2。
list1=[9, 6, 8, 4, 7]

def insert_sort(alist):
    #从第二个位置，即下标为1的元素开始向前插入
    for i in range(1,len(alist)):
        flag = False
        #第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                flag = True
            if flag:
                break
        print(alist)

insert_sort(list1)