#-*-coding:utf-8 -*-
"""
@project:untitled
@File: 快速排序.py
@Time: 2019/10/28 10:45
@user：优就业-刘欢    
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        base = arr[0]
        less = [v for v in arr[1:] if v<=base]
        more = [v for v in arr[1:] if v>base]
        return quick_sort(less) + [base] + quick_sort(more)
lst = [1, 23, 74, 64, 3, 6, 2, 53, 57, 12]
print(quick_sort(lst))