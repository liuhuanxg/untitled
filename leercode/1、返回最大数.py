#-*-coding:utf-8 -*-
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
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

"""

class Solution:
    def largestNumber(self, nums):
        nums = [str(i) for i in nums]
        nums.sort(key=lambda x: x[0], reverse=True)
        return "".join(nums)
s = Solution()
s.largestNumber([3,30,34,5,9])
a = 10
b = 20
c = [a]
a = 15
print(c)

dict1 = {(1,1):11}
print(dict1)