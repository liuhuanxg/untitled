#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入一个括号对字符串，判断是否合法，括号只由(){}[]组成。
示例:
{}() 合法，
 {)(}不合法
"""


class Solution():
    def check(self, strings):
        mapping = {
            "}": "{",
            ")": "(",
            "]": "[",
        }
        queue = []
        if len(strings) % 2 != 0:
            return False
        for s in strings:
            if s not in mapping:
                queue.append(s)
            else:
                if mapping[s] != queue.pop():
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.check("{}()"))
    print(s.check("{()}"))
    print(s.check("{)(}"))
    print(s.check("{]"))
