#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 返回两数之和.py

给定数组：
    [2,7,11,15,7]
求和为9的数的下标
"""


# 暴力求解，时间复杂度On2
def two_sum(lst, target):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                return i, j


# 使用set求解On
def two_sum1(lst, target):
    set1 = set(lst)
    for i in set1:
        set1.remove(i)
        if target - i in set1:
            return lst.index(i), lst.index(target - i)


# 使用dict缓存
def two_sum2(lst, target):
    dct = {}
    for i in range(len(lst)):
        num = target - lst[i]
        if num in dct:
            return dct[num], i
        dct[lst[i]] = i


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in dct:
                return dct[num], i
            dct[nums[i]] = i

if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum1([2, 7, 11, 15], 9))
    print(two_sum2([2, 7, 11, 15], 9))
