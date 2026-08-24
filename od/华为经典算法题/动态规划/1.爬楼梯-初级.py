"""
爬楼梯（LeetCode 70，简单）— 动态规划
每次可爬 1 或 2 阶，n 阶楼梯共有多少种不同走法。
输入：n=1 -> 1
输入：n=2 -> 2
输入：n=3 -> 3
输入：n=5 -> 8

思路提示：
- 状态转移 dp[i] = dp[i-1] + dp[i-2]（最后一步走 1 阶或 2 阶），本质斐波那契；
- 用两个变量滚动即可把空间压到 O(1)。
"""


def climb_stairs(n):
    pass


if __name__ == '__main__':
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    print("all tests passed")
