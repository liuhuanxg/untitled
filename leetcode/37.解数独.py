#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 36-37数独.py
"""

"""
37. 解数独

编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。
"""


class Solution():

    def start_check(self, sudo):
        if not sudo:
            return
        self.sudoku(sudo, 0)
        return sudo

    def sudoku(self, sudo, count):
        for i in range(9):
            for j in range(9):
                if sudo[i][j] == 0:
                    for k in range(1, 10):
                        if self.check_valid(sudo, i, j, k):
                            sudo[i][j] = k
                            count += 1
                            if self.sudoku(sudo, count):
                                return True
                            else:
                                sudo[i][j] = 0
                    # count -= 1
                    return False
        return True

    def check_valid(self, sudo, i, j, k):
        """"""
        x, x_alias = i % 3, i // 3
        y, y_alias = j % 3, j // 3
        nums = []
        for a in range(3):
            for b in range(3):
                nums.append(sudo[x_alias * 3 + a][y_alias * 3 + b])
        if k not in sudo[i] and k not in [y[j] for y in sudo] and k not in self.get_9_numbers(sudo, i, j):
            return True
        return False

    def get_9_numbers(self, sudo, i, j):
        # TODO-可以优化，将某个块的值存储在字典中，下次不用重新查询
        x_alias = i // 3
        y_alias = j // 3
        nums = []
        for a in range(3):
            for b in range(3):
                nums.append(sudo[x_alias * 3 + a][y_alias * 3 + b])
        return nums


if __name__ == '__main__':
    arr = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    """
    00 01 02  
    10 11 12
    20 21 22
    30 31 32
    40 41 42
    """
    s = Solution()
    # s.get_9_numbers(arr, 6, 0)
    for d in s.start_check(arr):
        print(d)
    print("="*10)
    # d = [
    #     [7, 6, 1, 0, 3, 0, 0, 2, 5],
    #     [3, 5, 0, 0, 0, 8, 1, 0, 7],
    #     [0, 2, 0, 0, 0, 7, 0, 3, 4],
    #     [0, 0, 9, 0, 0, 6, 3, 7, 8],
    #     [0, 0, 3, 2, 7, 9, 5, 8, 0],
    #     [5, 7, 0, 3, 0, 0, 9, 0, 2],
    #     [1, 9, 5, 7, 6, 0, 0, 0, 0],
    #     [8, 3, 2, 4, 0, 0, 7, 6, 0],
    #     [6, 4, 7, 0, 1, 0, 2, 5, 0]]
    # for s in s.start_check(d):
    #     print(s)
