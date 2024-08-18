#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 69求解某个数的平方根.py

给定一个数，求解该数的平方根，保留若干位小数
"""


class Solution():
    def find_qurt(self, number, n):
        left = 1
        right = number
        while right - left > n:
            mid = (left + right) /2
            if mid ** 2 > number:
                right = mid
            elif mid ** 2 < number:
                left = mid
            else:
                return mid
        return (right+left)/2

if __name__ == '__main__':
    s = Solution()
    print(s.find_qurt(4, 10**-2))
    print(s.find_qurt(5, 10**-2))
    print(s.find_qurt(6, 10**-2))
    print(s.find_qurt(9, 10**-2))
