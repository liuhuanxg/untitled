#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 35.搜索插入位置.py
Created Time: 2024/8/15 22:21
"""

"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

 

示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2

示例 2:
输入: nums = [1,3,5,6], target = 2
输出: 1

示例 3:
输入: nums = [1,3,5,6], target = 7
输出: 4

提示:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为 无重复元素 的 升序 排列数组
-104 <= target <= 104

使用二分法查找
"""


class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            # mid = (right + left) // 2
            # if nums[mid] < target:
            #     left = mid + 1
            # elif nums[mid] == target:
            #     return mid
            # else:
            #     right = mid - 1

            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1  # 范围缩小到 [mid+1, right]
            else:
                right = mid - 1  # 范围缩小到 [left, mid-1]

        return left


if __name__ == '__main__':
    s = Solution()
    # print(s.searchInsert([1, 3, 5, 6], 7))
    print(s.searchInsert([1, 3, 5, 6], 2))
    # assert s.searchInsert([1, 3, 5, 6], 5) == 2
    # assert s.searchInsert([1, 3, 6], 5) == 2
    # assert s.searchInsert([1, 3, 5, 6], 7) == 4
