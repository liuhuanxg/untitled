#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 72编辑距离.py

给定两个单词，从单词1变为单词2，求最少需要多少步操作，可以插入、删除、替换
例如：
    horse ros           需要3步
    intention nation    需要4步

方法：
    1. 暴力求解 DFS
    2. DP方程
        状态定义 DP[i][j] word1的前i个字符要替换为word2的前j个字符，最少需要的步数
        DP方程 DP[m][n]，m表示word1的长度，n表示word2的长度。

            dp[i,j] =  if word1[:i] == word2[:j]:
                            dp[i-1,j-1]
                        else: insert, delete, replace
                        1 + Min(DP[i-1,j], DP[i, j-1], DP[i-1, j-1])
"""


class Solution():
    def min_distance(self, word1, word2):
        """

        DP[i][j] word1的前i个字符要替换为word2的前j个字符，最少需要的步数
        所以DP[0][0]表示不替换，为0
        DP[0][1]表示要在word2中进行1次操作，为1，同理DP[0][2]表示进行2次操作
        同理DP[1][0] 表示在word1中进行1次操作，为1，
        取出三者的最小值，记为当前操作过程中的最小值
        [
            [0, 1, 2, 3],
            [1, 0, 0, 0],
            [2, 0, 0, 0],
            [3, 0, 0, 0]
        ]

        :param word1: 第一个单词
        :param word2: 第二个单词
        :return:
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = min(
                    dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
                    dp[i - 1][j] + 1,
                    dp[i][j - 1] + 1
                )
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.min_distance("ros", "ros"))
    print(s.min_distance("horse", "ros"))
    print(s.min_distance("intention", "nation"))
