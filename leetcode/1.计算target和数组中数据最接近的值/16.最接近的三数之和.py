#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 16.最接近的三数之和.py

给你一个长度为 n 的整数数组nums和 一个目标值target。请你从 nums 中选出三个整数，使它们的和与target最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/3sum-closest

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

输入：nums = [0,0,0], target = 1
输出：0


"""


# class Solution():
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         if 3 > len(nums) or len(nums) > 1000:
#             return 0
#         nums.sort()
#         min_sum = target - nums[0] - nums[1] - nums[2]
#         for i in range(1, len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 for k in range(j + 1, len(nums)):
#                     if abs(target - nums[i] - nums[j] - nums[k]) < abs(min_sum):
#                         min_sum = target - nums[i] - nums[j] - nums[k]
#         return target - min_sum


class Solution():
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if 3 > len(nums) or len(nums) > 1000:
            return 0
        nums.sort()
        min_diff = abs(target - nums[0] - nums[1] - nums[2])
        ans = nums[0] + nums[1] + nums[2]
        for i, v in enumerate(nums[:-2]):
            # 相同的元素只计算一次
            if i >= 1 and v == nums[i - 1]:
                continue
            s = v + nums[i + 1] + nums[i + 2]
            if s > target:
                if s - target < min_diff:
                    ans = s
                break

            s = v + nums[-1] + nums[-2]
            if s < target:
                if abs(target - s) < min_diff:
                    min_diff = target - s
                    ans = s
                continue
            first, last = i + 1, len(nums) - 1
            while first < last:
                s = v + nums[first] + nums[last]
                if s == target:
                    return s
                elif s > target:
                    last -= 1
                else:
                    first += 1
                if abs(target - s) < min_diff:
                    min_diff = abs(target - s)
                    ans = s
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))
    print(s.threeSumClosest([0, 0, 0], 1))
    print(s.threeSumClosest([4, 0, 5, -5, 3, 3, 0, -4, -5], 1))
    # print(s.threeSumClosest([0, 0, 0], 1))
    # print(s.threeSumClosest([1, 1, 1, 0], -100))
