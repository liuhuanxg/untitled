#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 5.最长回文字符串.py

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案
输入：s = "cbbd"
输出："bb"

方法1：暴力循环，到某个位置时，就遍历当前位置到结束位置的所有子串，然后与已知的最长子串比较，取最长的子串
方法2：
"""


class Solution:
    def longestPalindrome1(self, s: str) -> str:
        ret = ""
        for i in range(len(s)):
            string = ""
            for j in range(i, len(s)):
                string += s[j]
                if string == string[::-1] and len(ret) < len(string):
                    ret = string
        return ret

    def longestPalindrome(self, s: str) -> str:
        """
        每次到
        :param s:
        :return:
        """
        ret = ""
        for i in range(len(s)):
            string = ""
            for j in range(i, len(s)):
                string += s[j]
                if string == string[::-1] and len(ret) < len(string):
                    ret = string
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome("b"))
