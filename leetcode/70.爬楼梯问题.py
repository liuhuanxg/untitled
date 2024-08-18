#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 70.爬楼梯问题.py

给定楼梯的高度，每次只能走1步或者两步，计算总共可能走的方案，类似斐波那契
1. 回溯计算
    f(n) = f(n-1)+f(n-2)
    a. DP状态的定义
    b. DP方程

2. 斐波那契数列计算
    台阶高度为1，方案为
    1
    台阶高度为2，方案为
    1 1
    2
    台阶高度为3，方案为
    1 1 1
    1 2
    2 1
    4，方案为
    1 1 1 1
    1 1 2
    1 2 1
    2 1 1
    2 2
"""


class Solution():

    def fib(self, n):
        a = 0
        b = 1
        c = 1
        for _ in range(0, n):
            c = a + b
            a, b = b, c
        return c

    def fib2(self, n):
        mapping = {0: 0, 1: 1}
        for i in range(2, n + 1):
            mapping[i] = mapping[i - 1] + mapping[i - 2]
        return mapping[n]

    def tib2(self, n):
        mapping = {0: 0, 1: 1, 2: 1}
        for i in range(3, n + 1):
            mapping[i] = mapping[i - 1] + mapping[i - 2] + mapping[i - 3]
        return mapping[n]


if __name__ == '__main__':
    s = Solution()
    # print(s.fib(0))
    # print(s.fib(1))
    # print(s.fib(2))
    # print(s.fib(3))
    # print(s.fib(4))

    # print(s.fib2(0))
    # print(s.fib2(1))
    # print(s.fib2(2))
    # print(s.fib2(3))
    # print(s.fib2(4))

    print(s.tib2(0))
    print(s.tib2(1))
    print(s.tib2(2))
    print(s.tib2(3))
    print(s.tib2(4))
