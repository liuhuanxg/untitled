#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 169.求数组中的众数.py

给定一个数组，求数组中某个元素x使得
count(x)>n/2
例：[1,3,3,2,3] 返回3
例：[1,1,1,0,2] 返回1
"""


def main(arr):
    dct = {}
    for i in arr:
        count = dct.get(i, 0) + 1
        dct[i] = count
        if count > len(arr) // 2:
            return i


if __name__ == '__main__':
    print(main([1, 3, 3, 2, 3]))
    print(main([1, 1, 1, 0, 2]))
