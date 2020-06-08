#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 5、归并排序.py
@Time: 2020/5/19 9:53
@user：liuhuan   
"""

"""
归并排序和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好得多。但是需要额外的内存空间。

归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法的一个非常典型的应用。

归并排序是一种稳定的排序方法。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。
若将两个有序表合并成一个有序表，称为2-路合并

时间复杂度平均为O(nlog2n),最好为O(nlog2n),最坏O(nlog2n)，空间复杂度为O(n)，稳定排序
"""

"""
def merge_sort(data):
    half_index = int(len(data)/2)  # 将数据拆分

    alist1 = data[:half_index]
    alist2 = data[half_index:]

    if len(alist1)>1:
        alist1 = merge_sort(alist1)

    if len(alist2)>1:
        alist2 = merge_sort(alist2)

    index = 0
    for i in range(len(alist2)):
        state = 1
        for j in range(index,len(alist1)):
            if alist2[i]<alist1[j]:
                state = 0
                index = j + 1
                alist1.insert(j, alist2[i])
                break
        if state == 1:
            alist1.extend(alist2[i:])
            break
    return alist1
"""


# 实现由小扩展到大的子序列
def list_sort(d0, d1):  # 基元组往大扩展
    index = 0
    for i in range(len(d1)):  # 遍历d1数组
        state = 1
        for j in range(index, len(d0)):  # 遍历d0数组
            if d0[j] > d1[i]:
                state = 0
                index = j + 1
                d0.insert(j, d1[i])
                break
        if state == 1:  # 如果大于d0这个队列的所有值，那么直接extend所有数据
            d0.extend(d1[i:])
            break
    return d0


def merge_sort(data):
    d0 = [[x] for x in data]
    while len(d0) != 1:    # 循环条件
        length = len(d0)
        half = int(length/2)    # 除2的整数部分
        quo = length%2          # 除2的商
        d0_mid = []
        for i in range(half):
            d0_mid.append(list_sort(d0[i*2], d0[i*2+1]))
        if quo:
            d0_mid.append(d0[-1])
        d0 = d0_mid

    return d0[0]


if __name__ == "__main__":
   alist = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]  # 原始乱序
   d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]  # 正确排序
   d1 = merge_sort(alist)
   print(d0_out)