#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 29.两数相除.py
Created Time: 2024/8/14 22:01
"""

"""
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。

整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。

返回被除数 dividend 除以除数 divisor 得到的 商 。

注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。本题中，如果商 严格大于 231 − 1 ，则返回 231 − 1 ；如果商 严格小于 -231 ，则返回 -231 。


示例 1:
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = 3.33333.. ，向零截断后得到 3 。


示例 2:
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = -2.33333.. ，向零截断后得到 -2 。
 

提示：

-231 <= dividend, divisor <= 231 - 1
divisor != 0

"""


class Solution:
    # def divide(self, dividend, divisor):
    #     flag = True
    #
    #     max_val = 2 ** 31
    #     if dividend > max_val - 1:
    #         dividend = max_val - 1
    #     elif dividend < -max_val:
    #         dividend = -max_val
    #     if divisor > max_val - 1:
    #         divisor = max_val - 1
    #     elif divisor < -max_val:
    #         divisor = -max_val
    #
    #     if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
    #         flag = False
    #
    #     if abs(divisor) == 1:
    #         i = abs(dividend)
    #     else:
    #         i = 0
    #         while abs(dividend) >= abs(divisor):
    #             dividend = abs(dividend) - abs(divisor)
    #             i += 1
    #     ret = i if flag else -i
    #     if ret > - 1:
    #         ret = max_val - 1
    #     elif ret < -max_val:
    #         ret = -max_val
    #     return ret

    def divide(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res


if __name__ == '__main__':
    s = Solution()
    # print(s.divide(10, 3))
    # print(s.divide(10, -3))
    # print(s.divide(-10, -3))
    # print(s.divide(-7, -3))
    # print(s.divide(7, -3))
    print(s.divide(-2147483648, -1))
    print(s.divide(-2147483648, 1))
