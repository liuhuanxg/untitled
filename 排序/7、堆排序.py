#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 7、堆排序.py
@Time: 2020/5/19 10:15
@user：liuhuan   
"""

"""
堆排序：是指利用堆这种数据结构所涉及的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子节点的键值或索引总是大于或者小于它的父节点

时间复杂度平均为O(nlog2n),最好为O(nlog2n),最坏O(nlog2n)，空间复杂度为O(1)，不稳定排序
"""

d0 = [99, 5, 36, 7, 22, 17, 46, 12, 2, 19, 25, 28, 1, 92]


def sort_max(data):  # 直接冒泡一下吧,小到大
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def heap_min(data,type):
    index = 0
    if not type:
        for i in range(len(data[1:])):
            if data[index] > data[i+1]:
                index = i+1
        data[0],data[index] = data[index],data[0]
        return data
    else:
        for i in range(len(data[1:])):
            if data[index] < data[i+1]:
                index = i+1
        data[0],data[index] = data[index],data[0]
        return data


# d0 = [3,2,1,10,3]
# print(heap_min(d0,1))
# print(heap_min(d0,0))

import numpy as np


def heap_adj(data, type):  # data 原始堆，type=1最大堆，type=0最小堆
    length = len(data)
    floor = int(np.log2(length))
    for i in range(floor, 0, -1):  # 3（7 6 5 4）-2（3 2）-1（1）
        for j in range(2 ** floor - 1, 2 ** (floor - i) - 1, -1):
            # print(i,j)    # j-1 为当前父节点
            d_mid = [data[j - 1]]  # j = 7,j-1 =6 index
            if j * 2 <= length:  # 14
                d_mid.append(data[j * 2 - 1])
            if j * 2 + 1 <= length:
                d_mid.append(data[j * 2])

            d_mid = heap_min(d_mid, type)

            if len(d_mid) == 2:
                data[j - 1], data[j * 2 - 1] = d_mid[0], d_mid[1]
            elif len(d_mid) == 3:
                data[j - 1], data[j * 2 - 1], data[j * 2] = d_mid[0], d_mid[1], d_mid[2]
    return data

d1 = []
for i in range(len(d0)):
    data = heap_adj(d0, 0)
    d1.append(d0[0])
    del d0[0]


print(d1)