#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/median-of-two-sorted-arrays/

给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5


"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
       nums1右移的前提是nums1未走完，并且(nums1[l_start]<nums2[r_start]或者r_start全部走完)
       否则就nums2左移
        """
        m = len(nums1)
        n = len(nums2)
        total_length = n + m
        left, right = -1, -1
        l_start, r_start = 0, 0
        for _ in range(total_length // 2 + 1):
            left = right
            if l_start < m and (r_start >= n or nums1[l_start] < nums2[r_start]):
                right = nums1[l_start]
                l_start += 1
            else:
                right = nums2[r_start]
                r_start += 1

        return (right + left) / 2 if total_length % 2 == 0 else right


if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
