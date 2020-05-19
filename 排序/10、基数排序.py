#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 10、基数排序.py
@Time: 2020/5/19 11:23
@user：liuhuan   
"""

"""
基数排序(Radix Sort)是按照低位先排序，然后收集，再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。

基数排序基于分别排序，分别收集，所以是稳定的。

时间复杂度平均为O(d(r+n)),最好为O(d(n+rd)),最坏O(d(r+n))，空间复杂度为O(rd+n)，稳定排序

"""

d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]

d1 = [[] for x in range(10)]

# 第一次 最小位次排序
for i in d0:
    d1[i % 10].append(i)

print(d1)

d0_1 = []
for i in d1:
    if i:
        for j in i:
            d0_1.append(j)
print(d0_1)

# 第二次 次低位排序
d2 = [[] for x in range(10)]
for i in d0_1:
    d2[int(i/10)].append(i)
print(d2)

d0_2 = []
for i in d2:
    if i:
        for j in i:
            d0_2.append(j)
print(d0_2)