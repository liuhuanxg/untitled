# coding=utf8


class Solution():
    def __init__(self):
        self.dx = [0, 1, 0, 1]
        self.dy = [0, 0, -1, -1]

    def maxArea(self, height):
        start_index = 0
        end_index = len(height) - 1
        area = min(height[start_index], height[end_index]) * (end_index - start_index)
        i = 0
        while i <= end_index and start_index < end_index:
            area, index = self.check_value(start_index, end_index, height)
            start_index, end_index = index
            i += 1
        # print(start_index, end_index, area)

        return area

    def check_value(self, start_index, end_index, height):
        dct = {}
        for i in range(4):
            index1 = start_index + self.dx[i]
            index2 = end_index + self.dy[i]
            tmp_height = min(height[index1], height[index2]) * (index2 - index1)
            dct[tmp_height] = (index1, index2)
        values = sorted(dct.items(), key=lambda x: x[0], reverse=True)
        return values[0]


def recursion(level, param1, param2, *args):
    """
    递归模板
    1. 终止条件
    2. 业务处理
    3. 递归调用
    4. 还原之前的数据状态
    :param level:
    :param param1:
    :param param2:
    :param args:
    :return:
    """


visited = set()


def dfs(node, visited):
    """
    深度优先遍历
    :param node:
    :param visited:
    :return:
    """
    visited.add(node)
    for next_node in node.children():
        if node not in visited:
            dfs(next_node, visited)


def bfs(tree):
    """
    广度优先遍历
    :param tree: 遍历的树
    :return:
    """
    ret = []
    nodes = [tree.root]
    while nodes:
        level_size = len(nodes)
        # 存储这一层的所有node
        current_level_nodes = []
        current_level = []
        for _ in range(level_size):
            node = nodes.pop(0)
            current_level.append(node.val)
            if node.left:
                current_level_nodes.append(node.left)
            if node.right:
                current_level_nodes.append(node.right)
        nodes.extend(current_level_nodes)
        ret.append(current_level)


def search(arr, target):
    """
    二分查找，必须是有序数组
    :param arr: 有序数组
    :param target: 查找的目标
    :return:
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) / 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right -= 1
        else:
            left += 1


# dp方程
"""
dp状态定义
初始状态定义
DP状态推到
返回最优解
"""

def fn(n):
    return 1 if n < 2 else n * fn(n - 1)


def shell_sort(arr):
    n = len(arr)
    gap = 5

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # gap //= 2
        break
    print(arr)

    return arr


def func(s):
    lst = ["red", "yellow", "blue"]
    result = []
    for l in lst:
        result.append(check_value(s, l))
    return " ".join(result)
def check_value(s, child_s):
    if child_s in s:
        return "1"
    return "0"



def knapsack(V, n, vi, wi):
    # 初始化一个二维数组dp，其中dp[i][j]表示前i个物品中，体积不超过j的情况下，能装的最大价值
    dp = [[0 for _ in range(V + 1)] for _ in range(n + 1)]

    # 遍历所有物品
    for i in range(1, n + 1):
        # 遍历所有可能的体积
        for j in range(1, V + 1):
            # 如果当前物品的体积小于等于当前背包的剩余体积，那么可以选择装或不装
            if vi[i - 1] <= j:
                # 选择装当前物品和不装当前物品中，能装的最大价值较大的那个
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - vi[i - 1]] + wi[i - 1])
            else:
                # 如果当前物品的体积大于当前背包的剩余体积，那么只能选择不装
                dp[i][j] = dp[i - 1][j]

    # 返回最终结果，即背包能装的最大价值
    return dp[n][V]



if __name__ == '__main__':
    # s = Solution()
    # s.maxArea([1, 3, 2, 5, 4, 5, 2, 8])
    # s.maxArea([2, 3, 4, 5, 18, 17, 6])
    # send_alarm(1, {})
    # print(list(filter(lambda n: n % 3, range(6))))
    # print(list(map(fn, filter(lambda n: n % 3, range(6)))))
    # shell_sort([16, 25, 12, 30, 47, 11, 23, 36, 9, 18, 31])
    # print(func("redyellowblue"))
    # 示例
    V = 10
    n = 3
    vi = [2, 3, 4]
    wi = [3, 4, 5]
    print(knapsack(V, n, vi, wi))