#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 231-338-2的幂次方问题.py

题目1：判断一个数是否是2的n次幂
    3种方法：
    1. 每次/2，判断最后结果是否为1
    2. 计算log2是否为int
    3. 使用位运算 x&(x-1)

题目2：比特位计数：给定一个非负整数num，对于0<=i<=num范围内的每个数字i计算其二进制数中1的数目，并将它们作为数组返回。
例如输入：2 [0, 1, 1]
例如输入：3 [0, 1, 1, 2]

方法1：对每个数都计算1的个数count，时间复杂度O(n*count)的个数
方法2：count(n+1)
count(i) = count(i&(i-1)) + 1

"""


class Solution():

    def find_1_count(self, num):
        ret = [0]
        for i in range(1, num + 1):
            # ret.append(self.check_count(i))
            ret.append(ret[i & (i - 1)] + 1)
        return ret



if __name__ == '__main__':
    s = Solution()
    print(s.find_1_count(0))
    print(s.find_1_count(1))
    print(s.find_1_count(2))
    print(s.find_1_count(3))
    print(s.find_1_count(4))
