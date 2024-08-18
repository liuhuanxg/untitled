#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 152数组中子序列的最大乘积.py
给定一个数组，从中选取一个子序列，计算乘积最大值
例：
    [2,3,-2,4] 最大子序列为 [2, 3]
    [-2,0,-1] 最大子序列为 0
    [2,3,-10,5,-1] 最大子序列为 [2,3,-10,5,-1]
方法：
1. 使用递归暴力求解，循环所有的可能
2. DP方程
    1. 状态定义：从0开始一直探测到i，将可能存在的最大值记录一一但是要同时记录最大值和最小值
    2. DP状态转移方程，通过二维数组分别存储正数最大值及负数最小值，0表示最大值，1表示最小值：
        更新正的最大值
            DP[i, 0] =
                if a[i]>0:
                    DP[i-1,0]*a[i]
                else:
                    DP[i-1,1]*a[i]
        更新负的最小值：
            DP[i, 1] =
                if a[i]>0:
                    DP[i-1,1]*a[i]
                else:
                    DP[i-1,0]*a[i]

"""


class Solution():
    def find_max_sub_lst(self, nums):
        """
        比较：
            正值保留：当前值，上个值，上个值*当前值的最大者
            负值保留：当前值，上个值，上个值*当前值的最小者
        使用二维数组主要是为了更好的保留上个值的最大值及最小值
        :param lst:
        :return:
        """
        dp = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][1], dp[0][0], res = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x, y = i % 2, (i - 1) % 2
            # print("x:{},y:{},dp:{}".format(x, y, dp))
            dp[x][0] = max(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            dp[x][1] = min(dp[y][0] * nums[i], dp[y][1] * nums[i], nums[i])
            res = max(res, dp[x][0])
            # print("x:{},y:{},dp:{}".format(x, y, dp))
        return res

    def find_max_sub_lst2(self, nums):
        """
        比较：
            正值保留：当前值，上个值，上个值*当前值的最大者
            负值保留：当前值，上个值，上个值*当前值的最小者
        使用二维数组主要是为了更好的保留上个值的最大值及最小值
        :param lst:
        :return:
        """
        if not nums:
            return 0
        cur_min, cur_max, ret = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            value = nums[i]
            cur_min = cur_min * value
            cur_max = cur_max * value
            cur_min, cur_max = min(cur_min, value, cur_max), max(cur_min, value, cur_max)
            ret = cur_max if cur_max > ret else ret
        return ret


if __name__ == '__main__':
    s = Solution()
    # print(s.find_max_sub_lst([2, 3, -2, 4, 5, -1]))
    print(s.find_max_sub_lst([2, 3, -2, 4, 5]))
    print(s.find_max_sub_lst2([2, 3, -2, 4, 5]))
