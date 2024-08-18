#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
示例：
    给定二叉树[3,9,20,null,null,15,7]，返回其层次遍历结果
        3
    9       20
        15      7
    [
        [3],
        [9,20],
        [15,7],
    ]

可以用广度优先或者深度优先算法
"""
import collections


class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Tree():
    def __init__(self, node):
        self.root = node


# 广度优先遍历
# 遍历每一层级的时候，将该层级所有的元素全部遍历完之后再进入下一层级
def main(tree):
    ret = []
    nodes = [tree.root]
    # TODO:如果不是树需要判断该node是否已经处理过，但是Node不是一个iterable，不能set
    # visited = set(tree.root)
    while nodes:
        level_size = len(nodes)
        # 存储这一层的所有node
        current_level_nodes = []
        current_level = []
        for _ in range(level_size):
            node = nodes.pop(0)
            # if node not in visited:
            #     visited.add(node)
            current_level.append(node.val)
            if node.left:
                current_level_nodes.append(node.left)
            if node.right:
                current_level_nodes.append(node.right)
        nodes.extend(current_level_nodes)
        ret.append(current_level)
    print(ret)


class Solution(object):
    # 广度优先搜索
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

    # 深度优先搜索，使用递归的方式，先访问左节点，再访问右节点
    def dfs_start(self, root):
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node:
            return
        if len(self.result) < level + 1:
            self.result.append([])

        self.result[level].append(node.val)
        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)


if __name__ == '__main__':
    tree = Tree(
        Node(3,
             Node(9, None, None),
             Node(20,
                  Node(15, None, None),
                  Node(7, None, None))
             )
    )
    main(tree)

    tree = Tree(
        Node(3,
             Node(9, Node(5, None, None), None),
             Node(20,
                  Node(15, None, None),
                  Node(7, None, None))
             )
    )
    main(tree)
    n = Node(3,
             Node(9, Node(5, None, None), None),
             Node(20,
                  Node(15, None, None),
                  Node(7, None, None))
             )
    s = Solution()
    print(s.levelOrder(n))
    print(s.dfs_start(n))
