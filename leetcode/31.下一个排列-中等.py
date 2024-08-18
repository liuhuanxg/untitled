#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 31.下一个排列.py
Created Time: 2024/8/14 22:33
"""

"""
整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。

例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。

例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
给你一个整数数组 nums ，找出 nums 的下一个排列。

必须 原地 修改，只允许使用额外常数空间。

 
示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]

示例 3：
输入：nums = [1,1,5]
输出：[1,5,1]
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""

"""
思路：
第一步，倒序遍历查找到第一个降序的元素。
第二步，第二次倒序遍历找到第一个大于降序元素的元素
第三步，对第一个降序元素之后升序排列
"""


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i != 0:
            j = len(nums) - 1
            while nums[j] <= nums[i - 1]:
                print(i, j)
                j -= 1

            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        nums[i:] = sorted(nums[i:])
        print(nums)


if __name__ == '__main__':
    s = Solution()
    # s.nextPermutation([1, 2, 3])
    # s.nextPermutation([3, 2, 1])
    # s.nextPermutation([1, 5, 1])
    s.nextPermutation([1, 2, 5, 1])
