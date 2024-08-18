#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 120.二维数组最小路径.py

给定三角形（二维数组结构），求自顶向下的最小路径和，向下走的过程中只能走下层的相邻的两条路径。
例，从5走，只能走1和8, 加入当前坐标为[i,j]，则只能走[i+1,j], [i+1,j+1]
    [2]
    [3,4]
    [6,5,7]
    [4,1,8,3]

最短路径为2+3+5+1=11

方法：
    1. 递归的方式求解，不断递归求出所有的路径，时间复杂度O(2的n次方)
        traverse(i,j){
            traverse(i+1,j)
            traverse(i+1,j+1)
        }
    2. 贪心算法。简单贪心可能得到错误答案
    3. DP（动态规划问题）：从下向上推，时间复杂度O(m*n)，空间复杂度O(m*n)
        定义：将dp[i,j]各个point中最小的值进行存储。
        方程：
        dp[i,j] = min(dp[i+1, j], dp[i+1, j+1]) + point(i, j)
        最下一行的所有值都等于本身

"""


class Solution():

    def __init__(self):
        self.min_sum = 0

    def find_min_path(self, arr):
        """
        使用原数组,
        TODO: 可以优化只使用一个数组
        :param arr:
        :return:
        """
        for i in range(len(arr) - 1 - 1, -1, -1):
            for j in range(len(arr[i]) - 1, -1, -1):
                value = min(arr[i + 1][j], arr[i + 1][j + 1]) + arr[i][j]
                arr[i][j] = value
        return arr

    def find_min_path2(self, arr):
        """
        不使用原数组
        :param arr:
        :return:
        """
        dp_arr = []
        for i in range(len(arr) - 1, -1, -1):
            this_row_values = []
            for j in range(len(arr[i]) - 1, -1, -1):
                if i == len(arr) - 1:
                    this_row_values.insert(0, arr[i][j])
                else:
                    value = min(dp_arr[0][j], dp_arr[0][j + 1]) + arr[i][j]
                    this_row_values.insert(0, value)
            dp_arr.insert(0, this_row_values)
        return dp_arr

    def find_min_path3(self, arr):
        self.dfs(arr, 0, 0, 0, "")
        return self.min_sum

    def dfs(self, arr, i, j, sum, path):
        """
        TODO：遍历所有路径，最后求出最短路径
        :param arr: 二维数组
        :param i: 横坐标
        :param j: 纵坐标
        :param sum: 最后的求和
        :return: 返回的最短路径
        """
        if i == len(arr) - 1:
            sum += arr[i][j]
            path += str(arr[i][j]) + "#" + str(sum)
            if j == 0:
                self.min_sum = sum
            if sum < self.min_sum:
                self.min_sum = sum
            print(path)
            return sum
        sum += arr[i][j]
        path += str(arr[i][j]) + ">"
        self.dfs(arr, i + 1, j, sum, path)
        self.dfs(arr, i + 1, j + 1, sum, path)
        return sum


if __name__ == '__main__':
    s = Solution()
    arr = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    # print(s.find_min_path(arr))
    # print(s.find_min_path2(arr))
    arr = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(s.find_min_path3(arr))
