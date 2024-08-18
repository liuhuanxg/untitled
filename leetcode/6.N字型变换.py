#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 6.N字型变换.py

链接：https://leetcode.cn/problems/zigzag-conversion

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行Z 字形排列。

比如输入字符串为 "PAYPALISHIRING"行数为 3 时，排列如下：
P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

输入：s = "A", numRows = 1
输出："A"
两种情况时flag需要转向：
1. j<=0,flag=1
2. j>=numRows-1

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lst = [[] for _ in range(numRows)]
        j = 0
        flag = 1
        for i in range(len(s)):
            if j <= 0:
                flag = 1
            elif j >= numRows - 1:
                flag = -1
            lst[j].append(s[i])
            j += flag
        return "".join(["".join(l) for l in lst])


if __name__ == '__main__':
    s = Solution()
    print(s.convert("AB", 1))
    print(s.convert("PAYPALISHIRING", 3))
    print(s.convert("PAYPALISHIRING", 4))
