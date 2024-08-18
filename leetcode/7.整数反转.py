#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 7.整数反转.py

链接：https://leetcode.cn/problems/reverse-integer

给你一个32位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过32位的有符号整数的范围[−2的31次方, 2的31次方-1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）

输入：x = 123
输出：321

输入：x = -123
输出：-321

输入：x = 120
输出：21

输入：x = 0
输出：0
"""


class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        flag = False
        if x.startswith("-"):
            x = x[1:]
            flag = True
        x = int(x[::-1]) if not flag else -int(x[::-1])
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        return x


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(2**32))
    print(s.reverse(120))
    print(s.reverse(0))
