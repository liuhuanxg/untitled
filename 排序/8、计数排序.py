#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 8、计数排序.py
@Time: 2020/5/19 10:38
@user：liuhuan   
"""

"""
计数排序(Counting Sort)——字典计数-还原


计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数

计数排序是一种稳定的排序算法。计数排序使用一个额外的数组C，其中第i个元素是待排序数组A中值等于i的元素的个数。
然后根据数组C来将A中的元素排到正确的位置。它只能对整数进行排序。

时间复杂度为O(n+k),k代表整数的范围，最好最坏的情况相同。

空间复杂度为O(k)
"""
d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
d0_out = [2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7, 9, 12, 15, 44, 45, 54, 64]

d_max = 0
d_min = 0
for i in d0:
    if d_max<i:
        d_max = i
    if d_min>i:
        d_min = i

d1 = {}
for i in d0:
    if i in d1.keys():
        d1[i] += 1
    else:
        d1[i] = 1

d2 = []
for i in range(d_min,d_max+1):
    if i in d1.keys():
        for j in range(d1[i]):
            d2.append(i)

print(d2)