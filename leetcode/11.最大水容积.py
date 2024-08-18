#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1


提示：

n == height.length
2 <= n <= 105
0 <= height[i] <= 104


"""
class Solution():
    def maxArea(self, height):
        start_index = 0
        end_index = len(height) - 1
        max_value = min(height[start_index], height[end_index]) * (end_index - start_index)
        while start_index < end_index:
            if height[start_index] < height[end_index]:
                start_index += 1
            else:
                end_index -= 1
            max_value = max(max_value, min(height[start_index], height[end_index]) * (end_index - start_index))
        return max_value


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1, 3, 2, 5, 4, 5, 2, 8]))
    print(s.maxArea([2, 3, 4, 5, 18, 17, 6]))
    print(s.maxArea([6, 3, 4, 5, 18, 2, 3]))
