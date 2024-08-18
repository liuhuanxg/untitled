#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 10正则表达式匹配.py

给你一个字符串s和一个字符规律p，请你来实现一个支持 '.'和'*'的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/regular-expression-matching

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

"""


class Solution():
    def isMatch(self, s: str, p: str) -> bool:
        l1 = len(s)
        l2 = len(p)
        if l1 > 20 or l1 < 1 or l2 > 20 or l2 < 1:
            return False
        i1 = 0
        i2 = 0
        while i1 < l1:
            print(i1, i2, s[i1], p[i2])
            if i2 >= l2:
                return False
            if p[i2] == s[i1] or p[i2] == ".":
                i2 += 1
            elif p[i2] == "*":
                if (p[i2 - 1] != s[i1] and p[i2 - 1] != ".") or (
                    i1 + 1 < l1 and s[i1 - 1] != s[i1] and p[i2 - 1] != "."):
                    i2 += 1
                    continue
            elif p[i2] != s[i1]:
                if i2 + 1 < l2 and p[i2 + 1] == "*":
                    i2 += 2
                else:
                    return False
            i1 += 1
        if i2 == l2 and i1 == l1:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    assert s.isMatch("aa", "a") == False
    assert (s.isMatch("aa", "a*") == True)
    assert (s.isMatch("aab", "a*") == False)
    assert (s.isMatch("ab", ".*") == True)
    assert (s.isMatch("abcada", ".*") == True)
    assert (s.isMatch("aab", "c*a*b") == True)
    assert (s.isMatch("mississippi", "mis*is*ip*.") == True)
    # assert (s.isMatch("issippi", "is*p*.") == False)
    # assert (s.isMatch("ab", ".*c") == False)
    # assert (s.isMatch("aaa", "aaaa") == False)
