#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 15三数之和.py
Created Time: 2024/7/7 22:47
"""
"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 
提示：

3 <= nums.length <= 3000
-105 <= nums[i] <= 105


"""

"""
先对数组进行排序，然后比较当前值与下个值，以及倒数的值的关系，比较所有值的结果
"""
class Solution:
    def threeSum(self, nums):
        res = []
        n = len(nums)
        if not nums or n < 3:
            return res
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R = R - 1
                else:
                    L = L + 1
        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(s.threeSum([0, 0, 0]))
    print(s.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))
