#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[-1,0,1,2,-1,-4]
a+b+c=0
求a,b,c下标
三种方法：
1. 暴力求解 时间复杂度On3
2. 先循环两次，再用set，时间复杂度：On2
3. sort-find，先排序时间复杂度O(NlogN)，在比较O(n2)，总时间复杂度O(n2)
"""


# 2.使用两次循环和set求解
def three_sum2(nums, target):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        # 相同的元素只计算一次
        if i >= 1 and v == nums[i - 1]:
            continue
        d = {}
        for x in nums[i + 1:]:
            if x not in d:
                d[target - v - x] = 1
            else:
                res.add((v, -v - x, x))
    return res


# 在先对数组排序，然后i和length-i比较，如果比targe小，则length-i-1，否则i+1
def three_sum3(nums, target):
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        # 相同的元素只计算一次
        if i >= 1 and v == nums[i - 1]:
            continue
        first, last = i + 1, len(nums) - 1
        while first < last:
            if nums[first] + nums[last] < target - v:
                first += 1
            elif nums[first] + nums[last] > target - v:
                last -= 1
            else:
                res.add((v, nums[first], nums[last]))
                first += 1
                last += 1
    return res


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            # 相同的元素只计算一次
            if i >= 1 and v == nums[i - 1]:
                continue
            first, last = i + 1, len(nums) - 1
            while first < last:
                if nums[first] + nums[last] < 0 - v:
                    first += 1
                elif nums[first] + nums[last] > 0 - v:
                    last -= 1
                else:
                    res.add((v, nums[first], nums[last]))
                    first += 1
                    last -= 1
        return list(res)


if __name__ == '__main__':
    # print(three_sum2([-1, 1, 0, 4, 5, 9], 0))
    # print(three_sum2([2, 1, 0, 4, 5, 9], 0))
    # print(three_sum3([-1, 1, 0, -1, 5, 1], 0))
    # print(three_sum3([2, 1, 0, 4, 5, 9], 0))
    s = Solution()
    # print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    print(three_sum2([-1, 0, 1, 2, -1, -4], 0))
