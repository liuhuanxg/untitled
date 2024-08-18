#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 两数之和.py
Created Time: 2024/7/7 22:19
"""


class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
