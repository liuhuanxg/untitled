#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 322. 零钱兑换.py

零钱兑换：给定种类货币，返回最少需要多少个硬币拼成需要的数字，类似于上台阶问题
例如：
    [1,2,5] 拼成11
    [2]     拼成3

方法：
1. 暴力循环所有的可能，时间复杂度O(2的n次方)
2. 贪心算法：每次先选最大的，但是[1,6,7]这种不太适用
3. DP方程，时间复杂度为O(x*n)，空间复杂度为O(x)，x表示给定的面值。
    状态定义：DP[i]，上到i级台阶需要的最少步数
    DP方程：DP[i]= min(DP[i-coins[j]]) + 1
    因为所有的硬币种类存储在DP中，DP为[0,1,2,3,4,5,6]
    如果此时硬币为5，需要比较的硬币为6，则：min(DP[6-5]+1)正好符合


例如：[1, 2, 5]
1 1
2 11 2
3 111 12
4 1111 112 22
5 11111 1112 122 5
6 111111 11112 1122 222 15
"""


class Solution():
    def coin_change(self, coins, amount):
        """
        暴力求解：循环所有的可能，只要有一个符合就返回，时间复杂度2的n次方
        :param coins:
        :param amount:
        :return:
        """
        for i in range(amount // 7, -1, -1):
            for j in range((amount - i * 6) // 2, -1, -1):
                for k in range((amount - i * 6 - j * 2), -1, -1):
                    if i * 7 + 6 * j + k == amount:
                        return i, j, k

    def coin_change2(self, coins, amount):
        """
        DP 方程，每次走到当前值时，使用之前位置的最小值推出当前值。
        :param coins: 所有的硬币面值
        :param amount: 目标金额
        :return:
        """
        dp = [i for i in range(amount + 2)]
        # print(dp)
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    # 假设金额为5，i为5，此时一个5正好可以兑换5，所以只需要1个
                    # 假设金额为5，i为6，此时需要1个5+1个1，所以是2
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        # TODO——最后返回值不对
        print(dp)
        return dp[amount]


if __name__ == '__main__':
    s = Solution()
    # print(s.coin_change([1, 6, 7], 30))
    print(s.coin_change2([2, 5], 11))
    print(s.coin_change2([11, 2, 5], 11))
    print(s.coin_change2([11], 11))
    print(s.coin_change2([11], 11))
    print(s.coin_change2([3, 5], 14))
