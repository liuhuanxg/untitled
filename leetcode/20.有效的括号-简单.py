#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 20有效的括号.py

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true

示例 3：
输入：s = "(]"
输出：false

提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
"""


class Solution:
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False

        mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = list()
        for i in s:
            if stack and mapping.get(i, "") == stack[-1]:
                stack.pop()
            elif not stack and i in mapping:
                return False
            else:
                stack.append(i)
        return not stack


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
