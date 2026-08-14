"""
### 题目描述

给定一棵二叉树，获取第 k 层节点的不同值，按升序排列。

- n：节点数量
- vals：各节点的值
- edges：边列表 [parent, child]
- k：目标层级（0-indexed，根节点为第 0 层）

"""

from collections import defaultdict


class Solution:
    def GetKLevelValues(self, n, vals, edges, k):
        tree = defaultdict(list)
        childs = set()
        for parent, child in edges:
            tree[parent].append(child)
            childs.add(child)
        # tree = {0:[1, 2], 1:[3,4], 2:[5,6]}
        # childs = [1,2,3,4,5,6]
        root = -1
        for t in tree:
            if t not in childs:
                root = t
                break
        queue = [root]
        level = 0
        while queue:
            if level == k:
                return sorted(set(vals[node] for node in queue))
            next_queue = []
            for q in queue:
                next_queue.extend(tree[q])
            queue = next_queue
            level += 1
        return []


if __name__ == '__main__':
    s = Solution()
    # 用例1：基本二叉树
    print(s.GetKLevelValues(5, [1, 2, 3, 4, 5], [[0, 1], [0, 2], [1, 3], [1, 4]], 0))  # [1]
    print(s.GetKLevelValues(5, [1, 2, 3, 4, 5], [[0, 1], [0, 2], [1, 3], [1, 4]], 1))  # [2, 3]
    print(s.GetKLevelValues(5, [1, 2, 3, 4, 5], [[0, 1], [0, 2], [1, 3], [1, 4]], 2))  # [4, 5]

    # 用例2：同一层有重复值（测试去重）
    print(s.GetKLevelValues(6, [10, 5, 5, 3, 7, 3], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 1))  # [5]
    print(s.GetKLevelValues(6, [10, 5, 5, 3, 7, 3], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]], 2))  # [3, 7]
    #
    # # 用例3：单链
    print(s.GetKLevelValues(4, [1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]], 3))  # [4]
    # print(s.GetKLevelValues(4, [1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]], 4))  # []
    #
    # # 用例4：单节点
    # print(s.GetKLevelValues(1, [42], [], 0))  # [42]
    # print(s.GetKLevelValues(1, [42], [], 1))  # []
    #
    # # 用例5：多叉树
    # print(s.GetKLevelValues(6, [1, 2, 3, 2, 8, 8], [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5]], 1))  # [2, 3]
    # print(s.GetKLevelValues(6, [1, 2, 3, 2, 8, 8], [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5]], 2))  # [8]
    #
    # # 用例6：所有值相同
    # print(s.GetKLevelValues(5, [5, 5, 5, 5, 5], [[0, 1], [0, 2], [1, 3], [1, 4]], 2))  # [5]
    #
    # # 用例7：根节点不是编号0
    # print(s.GetKLevelValues(3, [3, 7, 10], [[2, 0], [2, 1]], 0))  # [10]
    # print(s.GetKLevelValues(3, [3, 7, 10], [[2, 0], [2, 1]], 1))  # [3, 7]
