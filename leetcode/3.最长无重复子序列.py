#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 3.最长无重复子序列.py

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

输入: s = "abcabcbb"
输出: 3
输入: s = "bbbbb"
输出: 1
输入: s = "pwwkew"
输出: 3

每次先计算出之前所有的字串，到当前位置时，判断当前子串是否在之前的set中，如果在之前的set，就从之前一直往后删。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        lookup = set()
        cur_len = 0
        left = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])

        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
