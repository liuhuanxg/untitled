#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 300最长上升子序列.py

给定一个数组，求数组中最长上升的子序列。不需要连续
示例：
[10, 9, 2, 5, 3, 7, 101, 18, 20]
返回: [2, 3, 7, 18, 20]

方法：
1.暴力求解， 时间复杂度O(2的n次方)
2.DP方程，时间复杂度O(n的平方)：
    1. 状态定义 DP[i]：从头 —— 元素i的最长子序列的长度，结果为max(DP[0], DP[1], ..., DPn-1])
    2. 状态转移方程：
        for i: 0 —— n-1
            DP[i] = max{[DP[j]}+1 (j从0到j-1，且a[j]<a[i])
        i: 0 ——> n-1
        j: 0 ——> i-1
3. 二分法。时间复杂度O(nlogn)
        a. 维护数组，LIS
        b. for i :0——>n-1
            每来一个新的元素，如果比LIS的最后一个小，则找到比他大的数据替换掉，如果比前一个大，则append到最后。
            用二分查找找应该插入的位置，时间复杂度O(logn)
        c. LIS的size()就为最长子序列长度
"""


class Solution():
    def find_sub_lst(self, arr):
        """
        使用时间复杂度O(nlogn)的算法
        :param arr:
        :return:
        """
        LIS = []
        for i in range(0, len(arr)):
            print(LIS)
            value = arr[i]
            if i == 0:
                LIS.append(value)
            else:
                start, end = 0, len(LIS) - 1
                if value >= LIS[end]:
                    LIS.append(value)
                elif value <= LIS[start]:
                    LIS[start] = value
                else:
                    index = self.search_index(LIS, value)
                    LIS[index] = value
        return len(LIS)

    def search_index(self, lst, value):
        """
        构建二分查找方法
        :param lst:
        :param value:
        :return:
        """
        start, end = 0, len(lst) - 1
        while start < end:
            mid = (start + end) // 2
            if lst[mid] > value:
                end = mid - 1
            elif lst[mid] < value:
                start = mid + 1
        return end

    def find_sub_lst2(self, lst):
        """
        先将截止到每一个数的最长的sub lst长度记录到列表中，
        到下一个数时与之前的最长进行比较
        :param lst: 需要统计的数组
        :return:
        """
        sub_lst = [1 for _ in lst]
        res = 1
        for i in range(1, len(lst)):
            for j in range(i):
                if lst[j] < lst[i]:
                    sub_lst[i] = max(sub_lst[i], sub_lst[j] + 1)
            res = max(res, sub_lst[i])
        print(sub_lst)
        return res


if __name__ == '__main__':
    arr = [10, 9, 2, 5, 3, 5, 101, 18, 20]
    s = Solution()
    # print(s.find_sub_lst(arr))
    print(s.find_sub_lst2(arr))
