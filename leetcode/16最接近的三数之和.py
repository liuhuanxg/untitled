#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 16最接近的三数之和.py
Created Time: 2024/7/7 23:33
"""

"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
返回这三个数的和。
假定每组输入只存在恰好一个解。
 
示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

示例 2：
输入：nums = [0,0,0], target = 1
输出：0
 

提示：
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""


class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]
        minimal = float('inf')
        for first in range(n - 2):
            second = first + 1
            third = n - 1

            # 剪枝：
            if nums[first] + nums[second] + nums[second + 1] > target:
                # 针对最小的third 都过于大了，就不必从最大试到最小了
                third = second + 1
            if nums[first] + nums[third - 1] + nums[third] < target:
                # 针对最大的second 都过于小了，就不必从最小试到最大了
                second = third - 1

            while second < third:
                total = nums[first] + nums[second] + nums[third]
                cur_diff = total - target
                # 双指针 确定合适的范围
                if cur_diff > 0:
                    third -= 1
                elif cur_diff < 0:
                    second += 1
                else:
                    # 能够恰好满足时，直接返回
                    return target

                diff = abs(cur_diff)

                # 取相差部分绝对值较小的情况
                if diff < minimal:
                    minimal = diff
                    res = total
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert s.threeSumClosest([0, 0, 0], 1) == 0
