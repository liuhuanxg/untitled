#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 2.滑动窗口最大值.py
"""

"""

滑动窗口的大小为3，返回一个每次3个数中的最大值
例：[-1,3,-1,-3,5,3,6]
返回的结果:
 [3, 3, 5, 5, 6]
 
 [-1]
 [-1,3] 
 [-1,3,-1] 3
 [3,-1,-3] 3
 [-1,-3,5] 5
 [-3,5, 3] 5
 [5, 3, 6] 5

[0,1,2,3]
 3-3
 
 
[0]
-1 ,-1, 3 ,0
[3]
-1 -4
"""


def func(arr, k):
    if not arr:
        return []
    window, result = [], []
    for i, x in enumerate(arr):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and arr[window[-1]] <= x:
            window.pop()
        window.append(i)
        if i >= k - 1:
            result.append(arr[window[0]])

    return result


# print(func([-1, 3, -1, -3, 5, 3, 6], 3))
# print(func([4, -1, 3, -1, -3, 5, 3, 6], 3)) # 这种case不通过，因为在3加入的时候会把4误删除
# print(func([4, -1, 4, 3, -3, 5, 3, 6], 3))


def func2(arr, k):
    if not arr:
        return []
    window, result = [], []
    for i, x in enumerate(arr):
        if i >= k and window[0] <= i - k:
            window.pop(0)
        while window and arr[window[0]] <= x:
            window.pop(0)
        window.append(i)
        if i >= k - 1:
            result.append(arr[window[0]])

    return result


print(func([4, -1, 3, -1, -3, 5, 3, 6], 3))
print(func2([-1, 3, -1, -3, 5, 3, 6], 3))
print(func2([4, -1, 3, -1, -3, 5, 3, 6], 3))
print(func2([4, -1, 4, 3, -3, 5, 3, 6], 3))
