#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 51-52n皇后问题.py
n皇后问题:
    皇后同一行不能有其他皇后，同一列不能有其他皇后，同一撇和同一捺不能有其他皇后

例
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0


0 1 0 0 0
0 0 0 1 0
1 0 0 0 0
0 0 1 0 0
0 0 0 0 1

做法：
    1.暴力计算所有能放的位置
    2.剪枝——使用数组标记影响的横-竖-撇-捺
        假设第一个q的下标为i,j，若i+j=c
        则横为i，竖为j，撇i+j=c,捺i-j=c
    3.使用位运算

"""


class Splution():
    def find_q(self, n, start_index):
        if n <= 2:
            return
        ret = [start_index]
        invalid_index = []

        invalid_x = [start_index[0]]
        invalid_y = [start_index[1]]
        invalid_index.extend(start_index)
        c_lst = [start_index[1] + start_index[0]]

        for i in range(n):
            if i in invalid_x:
                continue
            flag = False
            for j in range(n):
                if j in invalid_y:
                    continue

                if [i, j] in invalid_index:
                    continue

                if (i + j) in c_lst or (j - i) in c_lst:
                    continue

                ret.append([i, j])
                invalid_x.append(i)
                invalid_y.append(j)
                c_lst.append(j + i)
                flag = True
                break
            if flag:
                continue

        return ret

    def dfs(self, n, start_index):
        pass

    def totalNQueens(self, n):
        if n < 1:
            return []
        self.count = 0
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        if row >= n:
            self.count += 1
            return

        bits = (~(cols | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits  # 取到最低位的1
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            bits = bits & (bits - 1)


if __name__ == '__main__':
    arr = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    s = Splution()
    print(s.find_q(4, [0, 1]))
    print(s.find_q(5, [0, 1]))
    print(s.totalNQueens(5))
