#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 191.返回某个数2进制数中1的个数.py

给定1个数，计算二进制数中有多少个1
3 011 2
5 101 2
8 100 1


方法1：每次除以2，转换为二进制形式，再计算1的个数
方法2：每次x&(x-1)去除最后一位1，时间复杂度取决与1的个数
"""


class Solution():
    def find_1_count(self, x):
        """
        使用每次去除最后一个1的方式
        :param x:
        :return:
        """
        count = 0
        while x != 0:
            x = x & (x - 1)
            count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.find_1_count(3))
    print(s.find_1_count(5))
    print(s.find_1_count(8))
