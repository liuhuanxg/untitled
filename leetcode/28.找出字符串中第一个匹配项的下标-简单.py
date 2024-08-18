#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 28.找出字符串中第一个匹配项的下标.py
Created Time: 2024/8/14 21:44
"""

"""
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。

 

示例 1：
输入：haystack = "sadbutsad", needle = "sad"
输出：0
解释："sad" 在下标 0 和 6 处匹配。
第一个匹配项的下标是 0 ，所以返回 0 。

示例 2：
输入：haystack = "leetcode", needle = "leeto"
输出：-1
解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
 

提示：

1 <= haystack.length, needle.length <= 104
haystack 和 needle 仅由小写英文字符组成

"""


class Solution:
    def strStr(self, haystack, needle) -> int:
        if len(needle) > len(haystack):
            return -1
        index = -1
        start = 0
        i = 0
        while i < len(haystack):
            if start == len(needle):
                break
            if haystack[i] == needle[start]:
                if index == -1:
                    index = i
                start += 1
            else:
                i-=index
                index = -1
                start = 0
                continue
            i += 1
        # return haystack.find(needle)
        return index


if __name__ == '__main__':
    s = Solution()
    # print(s.strStr("sadbutsad", "sad"))
    # print(s.strStr("sadbutsad", "sadbutsad"))
    # print(s.strStr("sadbutsad", "sadbutsaddd"))
    # print(s.strStr("sadbutsad", "sd"))
    print(s.strStr("mississippi", "issip"))
