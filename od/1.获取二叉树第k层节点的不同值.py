"""
获取二叉树第 k 层节点的不同值

### 题目描述

给定一棵二叉树，获取第 k 层节点的不同值，按升序排列。

- n：节点数量
- vals：各节点的值
- edges：边列表 [parent, child]
- k：目标层级（0-indexed，根节点为第 0 层）

### 解题思路

**BFS 按层遍历**：

1. 根据 edges 构建父→子的邻接表
2. 找到根节点（不是任何节点的子节点）
3. BFS 逐层遍历，到第 k 层时收集该层所有节点的值
4. 去重 + 升序排列返回

"""
from collections import defaultdict


class Solution:
    def GetKLevelValues(self, n, vals, edges, k):
        # 构建邻接表（父→子）
        children = defaultdict(list)
        child_set = set()
        for parent, child in edges:
            children[parent].append(child)
            child_set.add(child)

        # 找根节点（没有出现在 child 中的节点）
        root = -1
        for i in range(n):
            if i not in child_set:
                root = i
                break
        print(children, child_set, root)
        # BFS 按层遍历
        queue = [root]
        level = 0

        while queue:
            if level == k:
                # 到达目标层，收集不同值并排序
                result = sorted(set(vals[node] for node in queue))
                return result

            next_queue = []
            for node in queue:
                for child in children[node]:
                    next_queue.append(child)

            queue = next_queue
            level += 1

        # k 超出树的深度
        return []

if __name__ == '__main__':
    s = Solution()
    # 用例1：基本二叉树
    # s.GetKLevelValues(5, [1, 2, 3, 4, 5], [[0, 1], [0, 2], [1, 3], [1, 4]], 0)  # [1]
    # s.GetKLevelValues(5, [1, 2, 3, 4, 5], [[0, 1], [0, 2], [1, 3], [1, 4]], 1)  # [2, 3]
    # s.GetKLevelValues(5, [1, 2, 3, 4, 5], [[0, 1], [0, 2], [1, 3], [1, 4]], 2)  # [4, 5]
    #
    # # 用例2：同一层有重复值（测试去重）
    # s.GetKLevelValues(6, [10, 5, 5, 3, 7, 3], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 1)  # [5]
    # s.GetKLevelValues(6, [10, 5, 5, 3, 7, 3], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 2)  # [3, 7]
    #
    # # 用例3：单链
    s.GetKLevelValues(4, [1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]], 3)  # [4]
    # s.GetKLevelValues(4, [1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]], 4)  # []
    #
    # # 用例4：单节点
    # s.GetKLevelValues(1, [42], [], 0)  # [42]
    # s.GetKLevelValues(1, [42], [], 1)  # []
    #
    # # 用例5：多叉树
    # s.GetKLevelValues(6, [1, 2, 3, 2, 8, 8], [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5]], 1)  # [2, 3]
    # s.GetKLevelValues(6, [1, 2, 3, 2, 8, 8], [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5]], 2)  # [8]
    #
    # # 用例6：所有值相同
    # s.GetKLevelValues(5, [5, 5, 5, 5, 5], [[0, 1], [0, 2], [1, 3], [1, 4]], 2)  # [5]
    #
    # # 用例7：根节点不是编号0
    # s.GetKLevelValues(3, [3, 7, 10], [[2, 0], [2, 1]], 0)  # [10]
    # s.GetKLevelValues(3, [3, 7, 10], [[2, 0], [2, 1]], 1)  # [3, 7]