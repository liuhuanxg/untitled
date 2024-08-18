#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 44.通配符匹配.py
Created Time: 2024/8/15 12:52
"""

"""
给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符序列（包括空字符序列）。
判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。
 
示例 1：
输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

示例 2：
输入：s = "aa", p = "*"
输出：true
解释：'*' 可以匹配任意字符串。

示例 3：
输入：s = "cb", p = "?a"
输出：false
解释：'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。

提示：

0 <= s.length, p.length <= 2000
s 仅由小写英文字母组成
p 仅由小写英文字母、'?' 或 '*' 组成
"""

"""
思路：
构建
m*n数组
从左上向右下判断
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s横，p纵
        # 土味拼音变量名
        zong = len(p) + 1  # 纵轴长度
        heng = len(s) + 1  # 横轴长度

        table = [[False] * heng for i in range(zong)]
        table[0][0] = True
        if s == "" and p.count("*") == len(p):
            return True

        if p.startswith("*"):
            table[1] = [True] * heng

        for m in range(1, zong):
            path = False  # 是否可以在该行使用*的特技
            for n in range(1, heng):
                if p[m - 1] == "*":  # m是表格的索引，但不是p的索引
                    if table[m - 1][0] == True:
                        table[m] = [True] * heng
                    if table[m - 1][n]:  # 只要顶上有了True，就可以开通*接下来的所有道路
                        path = True
                    if path:
                        table[m][n] = True
                elif p[m - 1] == "?" or p[m - 1] == s[n - 1]:  # 先判断字母是否符合
                    table[m][n] = table[m - 1][n - 1]  # 再看左上方格子是不是T

        return table[zong - 1][heng - 1]


if __name__ == '__main__':
    s = Solution()
    # assert s.isMatch("aa", "a") == False
    # assert s.isMatch("aa", "*") == True
    # assert s.isMatch("aa", "ab") == False
    # assert s.isMatch("aba", "ab*") == True
    # assert s.isMatch("cb", "?a") == False
    # assert s.isMatch("aa", "?") == False
    # assert s.isMatch("a", "?") == True
    assert s.isMatch(" ", "*******") == True
    assert s.isMatch("", "?") == False
    assert s.isMatch(" ", "?") == True
