#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 50.计算x的n次方.py

1.直接用库函数，时间复杂度为O(1)
2.循环暴力求解，时间复杂度O(n)
3.分治 n/2，时间复杂度为O(log2n)
"""


def pow1(x, n):
    if n >= 0:
        if n == 1:
            return x
        return x * pow(x, n - 1)
    else:
        if n == -1:
            return 1 / x
        return 1 / x * pow(x, n + 1)


def pow2(x, n):
    if not n:
        return 1
    if n < 0:
        return 1 / pow2(x, -n)
    if n % 2:
        return x * pow2(x, n - 1)
    return pow2(x * x, n / 2)


# 用位运算的方式
# 8 > 4 > 2> 1
"""
1000
100
10
1
"""


def pow3(x, n):
    if n < 0:
        x = 1 / x
        n = -n
    ret = 1
    while n:
        if n & 1:
            ret *= x
        x *= x
        n >>= 1
    return ret


# 使用//2的方式
def pow4(x, n):
    if n % 2:
        n -= 1
        ret = x
    else:
        ret = 1
    if n < 0:
        x = 1 / x
        n = -n

    while n > 1:
        x *= x
        n //= 2

    return ret * x


def main():
    print(pow4(2, 2))
    print(pow4(2, 3))
    print(pow4(2, 4))
    print(pow4(2, 10))
    print(pow4(2.1, 3))
    print(pow4(2, -2))


if __name__ == '__main__':
    main()
