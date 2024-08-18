#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 0动态规划.py
求蚂蚁穿过障碍物回到巢穴的路径数量
"""


class Solution():
    def __init__(self):
        self.mem = {}

    def find_road_count(self, arr):
        for i in range(len(arr) - 1, -1, -1):
            for j in range(len(arr[i]) - 1, -1, -1):
                if arr[i][j] == -1:
                    continue
                if i == len(arr) - 1 or j == len(arr[0]) - 1:
                    arr[i][j] = 1
                else:
                    x = arr[i + 1][j]
                    y = arr[i][j + 1]

                    if x == -1 and y == -1:
                        arr[i][j] = 0
                    else:
                        if x == -1:
                            x = 0
                        if y == -1:
                            y = 0
                        arr[i][j] = x + y
        return arr


if __name__ == '__main__':
    s = Solution()
    arr = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, -1, 0, 0, 0],
        [-1, 0, -1, 0, 0, -1, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, -1, 0, -1, 0],
        [0, -1, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for lst in s.find_road_count(arr):
        print(lst)
