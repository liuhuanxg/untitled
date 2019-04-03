'''
# 一、冒泡排序  为每两个连续的数字进行比较，第一次比较完之后最大的在最后
def bubbleSort(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
'''

#二、选择排序
'''
1、首先在未排序的序列中找到最小（大）值，存放到排序序列的起始位置
2、再从剩下未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
3、重复第二步，直到所有元素均排序完毕'''
'''
def selectionSort(arr):
    for i in range(len(arr)-1):
        #记录最小数的索引
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minIndex]:
                minIndex=j
        #i 不是最小数时，将i和最小数进行交换
        if i !=minIndex:
            arr[i],arr[minIndex]=arr[minIndex],arr[i]
    return arr
'''

'''
通过构建有序序列，对于未排序数据，在已排序序列中向前扫描，找到相对应的位置插入，插入排序和冒泡排序一样，也有一种优化算法，叫做拆半插入'''
'''
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex=i-1
        current=arr[i]
        while preIndex>=0 and arr[preIndex]>current:
            arr[preIndex+1]=arr[preIndex]
            preIndex-=1
        arr[preIndex+1]=current
    return arr
'''

#三、希尔排序
'''
希尔排序是非稳定排序算法'''

def shellSort(arr):
    import math
    gap=1
    while(gap<len(arr)/3):
        gap=gap*3+1
    while gap>0:
        for i in range(gap,len(arr)):
            temp=arr[i]
            j=i-gap
            while j>=0 and arr[j]>temp:
                arr[j+gap]=temp
                j-=gap
            arr[j+gap]=temp
        gap=math.floor(gap/3)
    return arr
if __name__ == '__main__':
    A=[3,44,38,15,36,26,27,2,19,44,46,47,48,50]
    #冒泡排序
    # s=bubbleSort(A)

    #选择排序
    # s=selectionSort(A)

    #插入排序
    # s=insertionSort(A)

    #希尔排序
    s=shellSort(A)
    print(s)
