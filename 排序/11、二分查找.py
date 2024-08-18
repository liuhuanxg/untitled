# -*-coding:utf-8 -*-
"""
@project:untitled
@File: 11、二分查找.py
@Time: 2020/5/31 15:15
@user：liuhuan   
"""
"""
具备条件：
    1、顺序列表
    最优时间复杂度O(1)，最坏为O(logn)
    
算法思想：以lst = [1, 3, 7, 8, 10, 11]为例  
    先有初始比较区间：[0-len(lst)]
    第一次比较中间值：7
        如果7比待比较的值大，则从[1,3]中取值
        如果7比待比较的值小，则从[8,9,10]中取值
    依次向下进行直到起始值大于终止值时结束    
"""


# 递归方法查找
def binary_chop(lst, number):
    if len(lst) < 1:
        return False
    last = len(lst)
    mid = last // 2
    if lst[mid] > number:
        lst = lst[0:mid - 1]
        return binary_chop(lst, number)
    elif lst[mid] < number:
        lst = lst[mid + 1:]
        return binary_chop(lst, number)
    else:
        return True


# 非递归方法
"""
def binary_chop(lst, number):
    last = len(lst)-1
    first = 0
    while last-first>=0:
        mid = (last+first)//2
        if lst[mid] > number:
            last = mid-1
        elif lst[mid] < number:
            first = mid+1
        else:
            return mid
    return False
"""

if __name__ == '__main__':
    lst = [1, 3, 7, 8, 10, 11]
    number = 4
    print(binary_chop(lst, number))
