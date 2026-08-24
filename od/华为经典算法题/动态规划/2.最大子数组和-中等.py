"""
最大子数组和（LeetCode 53，中等）— Kadane 算法
输入：[-2,1,-3,4,-1,2,1,-5,4] -> 6（子数组 [4,-1,2,1]）
输入：[1]                     -> 1
输入：[5,4,-1,7,8]            -> 23
输入：[-1,-2,-3]              -> -1（全为负时取最大单个元素）

思路提示：
- 局部最优 dp[i] = max(nums[i], dp[i-1] + nums[i])；
- 维护一个全局最大值，遍历一遍 O(n) 完成，空间可压到 O(1)。
"""


def max_sub_array(nums):
    pass


if __name__ == '__main__':
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    assert max_sub_array([-1, -2, -3]) == -1
    print("all tests passed")
