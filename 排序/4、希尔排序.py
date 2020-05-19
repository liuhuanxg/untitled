#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 4、希尔排序.py
@Time: 2020/5/19 9:43
@user：liuhuan   
"""

"""
希尔排序(shell sort)也是一种插入排序，它是简单插入排序经过改进之后的更高效的版本，也被称为缩小增量排序，它与插入排序的不同之处在于，他会优先比较距离较远的元素。

从大范围到小范围进行比较-交换

时间复杂度平均为O(n1.3),最好为O(n),最坏O(n2)，空间复杂度为O(1)，不稳定排序
"""

def insert_sort(alist):
    for i in range(1,len(alist)):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                break
    return alist


# shell排序
def shell_sort(alist):
    length = int(len(alist)/2)
    num = int(len(alist)/length)

    while 1:
        print("length:",length,"num:",num)
        for i in range(length):
            d_mid = []
            for j in range(num):
                d_mid.append(alist[i+j*length])

            d_mid = insert_sort(d_mid)

            for j in range(num):
                alist[i+j*length] = d_mid[j]
        # print("alist:",alist)

        length =  int(length/2)
        if length==0:
            return alist

        num = int(len(alist)/length)

if __name__ == '__main__':
    alist = [2, 15, 5, 9, 7, 6, 4, 12, 5, 4, 2, 64, 5, 6, 4, 2, 3, 54, 45, 4, 44]
    shell_sort(alist)
    # print(insert_sort(alist))


