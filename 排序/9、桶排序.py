#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 9、桶排序.py
@Time: 2020/5/19 10:42
@user：liuhuan   
"""

"""
桶排序(Bucket Sort)是计数排序的升级版，它利用函数的映射关系，高效与否的关键在于映射函数的确定。

桶排序的工作原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序）

平均时间复杂度为O(n+k)，最好情况为O(n+k)，最坏情况为O(n2)
空间复杂度为O(n+k)，稳定排序
"""

d0 = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]

d1 = [[] for x in range(10)]
for i in d0:
    d1[int(i/10)].append(i)

# print(d1)


for i in range(len(d1)):
    if d1[i] != []:
        d2 = [[] for x in range(10)]
        for j in d1[i]:
            d2[j%10].append(j)
        d1[i] = d2

# print(d1)

d3 = []
for i in d1:
    if i:
        for j in i:
            if j:
                for k in j:
                    if k:
                        d3.append(k)
print(d3)