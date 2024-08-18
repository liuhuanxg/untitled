# -*-coding:utf-8 -*-
"""
@project:untitled
@File: 1、返回最大数.py
@Time: 2020/5/31 21:49
@user：liuhuan   
"""
"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
9 5

"""


class CompareNumbers(str):
    def __lt__(x, y):
        ret = x + y > y + x
        print(x, y, ret)
        return ret


# class Solution:
#
#     def largestNumber(self, nums):
#         str_nums = [str(num) for num in nums]
#         print(str_nums)
#         str_nums = sorted(str_nums, key=CompareNumbers)
#         result = "".join(str_nums)
#
#         return result if result[0] != "0" else "0"

class Solution:

    def largestNumber(self, nums):
        str_nums = [str(num) for num in nums]
        max_length = len(max(str_nums, key=lambda x: len(x)))

        # def func(x):
        #     return x + "0" * (max_length - len(x))
        #
        # str_nums = sorted(str_nums, key=func, reverse=True)

        str_nums = sorted(str_nums, key=lambda x: x + "0" * (max_length - len(x)), reverse=True)
        result = "".join(str_nums)
        return result if result[0] != "0" else "0"


if __name__ == '__main__':
    s = Solution()
    assert s.largestNumber([3, 30, 34, 5, 9]) == "9534330"
    assert s.largestNumber([10, 2]) == "210"
    assert s.largestNumber([1, 2]) == "21"
    assert s.largestNumber([1, 1]) == "11"
    assert s.largestNumber([9, 0, 2]) == "920"
    assert s.largestNumber([0, 0, 00]) == "0"
