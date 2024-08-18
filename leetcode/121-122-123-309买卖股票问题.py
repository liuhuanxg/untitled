#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 122买卖股票问题.py

题目：
121：只能买入一次，利率最大化

122：给定一只股票的股价，每天可以买卖无数次，无交易手续费输出总盈利。
例：
[7,1,5,3,6,4] 输出7
[1,2,3,4,5] 输出4
[7,6,3,2] 输出0

解法：
1.DFS（深度递归） 时间复杂度：2的n次方
2.贪心法：第二天比当天高才会买入，否则不买入。时间复杂度O(n)
3.动态规划。时间复杂度O(n)

123. 最多只能买卖两次

309. 交易有冷却时间

188. 最多可以交易k次

714. 买入，卖出有手续费


买入、卖出k次：
    DP方程：
    状态的定义：MP[i] 第i天的最大利润
    状态转移方程：MP[i] = MP[i-1] + (-a[i])    买股票
                                + a[i]      卖股票

                MP[i, 0] = max
                                MP[i-1, 0] + a[i]  卖
                                MP[i-1, 1] - a[i]  买
                MP[i, 1] = max
                                MP[i-1, 1] + a[i]  卖
                                MP[i-1, 0] - a[i]  买
                MP[i][j][k] i表示天数，j表示买入或卖出，k表示已经交易的次数
        for i : 0-n-1
            for k: 0-k
                只能持有一只股票时：
                    分为两种情况：第i-1天没有，当天没有操作。第i-1天有，当天卖出
                    MP[i, k, 0] = max(MP[i-1, k, 0], MP[i-1, k-1, 1] + a[i])
                    分为两种情况：第i-1天有，当天没有操作。第i-1天没有，当天买入
                    MP[i, k, 1] = max(MP[i-1, k, 1], MP[i-1, k-1, 0] - a[i])
                考虑可以持有的股票为x时：
                    for j :0——x:
                        MP[i, k, j] = max(  MP[i-1, k, j] 不动
                                        MP[i-1,k-1,j+1] + a[i] 卖出
                                        MP[i-1, k-1,j-1] - a[i] 买入
                                        )

"""


class Solution():

    def maxProfit(self, prices):
        """
        分别定义为
            没有买入股票
            当天买入股票
            当天卖出股票
        :param prices: 股票价格
        :return:
        """
        if not prices:
            return 0

        res = 0
        profit = [[0 for _ in range(3)] for _ in range(len(prices))]

        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0

        for i in range(1, len(prices)):
            profit[i][0] = profit[i - 1][0]
            profit[i][1] = max(profit[i - 1][1], profit[i - 1][0] - prices[i])
            profit[i][2] = profit[i - 1][1] + prices[i]
            res = max(res, profit[i][0], profit[i][1], profit[i][2])
        return res

    def max_profit_122(self, arr):
        """
        122.给定一只股票的股价，每天可以买卖无数次，无交易手续费输出总盈利
        :param arr: 股价走势数据
        :return: 返回收益
        """
        q = []
        total = 0
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] > 0:
                if q:
                    q.pop()
                q.append(arr[i])
                total += arr[i + 1] - arr[i]
            elif arr[i + 1] - arr[i] < 0 and q:
                q.pop()
        return total

    def max_2_profit(self, prices):
        """
        最多只能交易两次，定义三维数组，分别表示
        天数，之前交易的次数，是否持有股票
        :return:
        """
        if not prices:
            return 0
        maxint = 0
        profit = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(len(prices))]
        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = -maxint, -maxint
        profit[0][2][0], profit[0][2][1] = -maxint, -maxint
        for i in range(1, len(prices)):
            profit[i][0][0] = profit[i - 1][0][0]
            profit[i][0][1] = max(profit[i - 1][0][1], profit[i - 1][0][0] - prices[i])

            profit[i][1][0] = max(profit[i - 1][1][0], profit[i - 1][0][1] + prices[i])
            profit[i][1][1] = max(profit[i - 1][1][1], profit[i - 1][1][0] - prices[i])

            profit[i][2][0] = max(profit[i - 1][2][0], profit[i - 1][1][1] + prices[i])
        end = len(prices) - 1
        return max(profit[end][0][0], profit[end][1][0], profit[end][2][0])


if __name__ == '__main__':
    s = Solution()
    print(s.max_profit_122([7, 1, 5, 3, 6, 4]))
    print(s.max_profit_122([1, 2, 3, 4, 5]))
    print(s.max_profit_122([7, 6, 3, 2]))
