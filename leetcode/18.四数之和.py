#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 18.四数之和.py
Created Time: 2024/8/12 22:51
"""

"""
18. 四数之和
中等
相关标签
相关企业
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

提示：

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        length = len(nums)
        if length < 4 or sum(nums[-4:]) < target:
            return result
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, length - 1
                while left < right:
                    # print(nums[i], nums[j], nums[left], nums[right])
                    if left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    tmp_sum = sum([nums[i], nums[j], nums[left], nums[right]])
                    if tmp_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                    elif tmp_sum > target:
                        right -= 1
                    else:
                        left += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(s.fourSum([2, 2, 2, 2, 2], 8))
    print(s.fourSum([0, 0, 0, 0], 0))
    print(s.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))
    print(s.fourSum(
        [-497, -480, -477, -470, -452, -448, -440, -412, -390, -381, -372, -372, -369, -366, -355, -346, -340, -337,
         -322, -321, -311, -296, -258, -249, -248, -232, -215, -199, -174, -154, -128, -122, -122, -117, -115, -113,
         -110, -89, -86, -84, -78, -71, -69, -53, -49, -35, -25, -21, -7, 3, 7, 21, 25, 30, 47, 52, 81, 84, 87, 91, 96,
         157, 161, 167, 178, 184, 210, 217, 228, 236, 274, 277, 283, 286, 290, 301, 302, 341, 352, 354, 361, 367, 384,
         390, 412, 421, 458, 468, 483, 484, 486, 487, 490, 491], -8377))
