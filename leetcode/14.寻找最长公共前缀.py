#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 14.寻找最长公共前缀.py
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
输入：strs = ["flower","flow","flight"]
输出："fl"

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。


"""


class Solution():
    def longestCommonPrefix(self, strs) -> str:
        min_length_str = min(strs, key=lambda x: len(x))
        ret = ""
        for i in range(len(min_length_str)):
            flag = True
            tmp_s = ""
            for s in strs:
                if s[i] != min_length_str[i]:
                    flag = False
                    break
                tmp_s = s
            if not flag:
                break
            ret += tmp_s[i]
        return ret


if __name__ == '__main__':
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["fight", "fighter", ""]) == ""
