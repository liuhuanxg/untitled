"""
冒泡排序：是一种简单的排序算法，重复的遍历要排序的序列，一次比较两个元素，如果他们的顺序错误就把他们的顺序交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该序列已经排序完成。算法名字的由来是因为越来越小的元素会经由交换慢慢的“浮”到数列的顶端。第一次排完之后最大的数在最后。

时间复杂度平均O(n2)，最好为O(n),最坏为O(n2),空间复杂度为O(1)，稳定排序
"""
list1=[9, 6, 8, 4, 7]
"""
for i in range(1,len(list1)):
    for j in range(len(list1)-i):
        if list1[j+1] < list1[j]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
    print(list1)
"""



# [6, 8, 4, 7, 9]
# [6, 4, 7, 8, 9]
# [4, 6, 7, 8, 9]
# [4, 6, 7, 8, 9]


# def bubble_sort(alist):
#     for j in range(len(alist)-1,0,-1):
#         #j表示每次便利需要比较的次数，逐渐缩小
#         for i in range(j):
#             if alist[i]>alist[i+1]:
#                 alist[i],alist[i+1] = alist[i+1],alist[i]
#         print(alist)
# bubble_sort(list1)


alist = [9, 6, 7, 5, 10, 3]
def bubble_sort(alist):
    for i in range(1, len(alist)):
        flag = False
        for j in range(len(alist)-i):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                flag = True
        if not flag:
            break
    print(alist)
bubble_sort(alist)
