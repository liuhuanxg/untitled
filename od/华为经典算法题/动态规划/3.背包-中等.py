"""
0-1 背包（经典动态规划）— 每种物品最多选一次
给定物品重量 weights、价值 values、背包容量 capacity，求能装下的最大价值。
weights=[1,3,4], values=[15,20,30], capacity=4 -> 35（选重量1和4：价值15+30）
weights=[2,3,4,5], values=[3,4,5,6], capacity=5 -> 7（选重量2和3：价值3+4）

思路提示：
- 二维 dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i]] + values[i])；
- 用逆序遍历把 dp 压缩为一维数组 dp[w]，空间 O(capacity)。
"""


def knapsack(weights, values, capacity):
    pass


if __name__ == '__main__':
    assert knapsack([1, 3, 4], [15, 20, 30], 4) == 35
    assert knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
    assert knapsack([1, 2, 3], [6, 10, 12], 5) == 22  # 选 2+3
    assert knapsack([2], [3], 1) == 0                 # 装不下
    print("all tests passed")
