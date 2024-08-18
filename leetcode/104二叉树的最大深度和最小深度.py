#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 104二叉树的最大深度和最小深度.py

题目：
    给定二叉树[3,9,20,null,null,15,7,null,4]
    返回它的最大深度4，最小深度2

广度优先或者深度优先

"""


class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Tree():
    def __init__(self, node):
        self.root = node


class Solution():

    # 深度优先
    def dfs(self, root):
        if not root:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))

    # 广度优先
    def bfs(self, root):
        if not root:
            return 0, 0
        queue = []
        queue.append(root)
        max_level = 0
        min_level = 0
        while queue:
            max_level += 1
            current_level_node = []
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                if (not node.left or not node.right) and min_level == 0:
                    min_level = max_level
                if node.left:
                    current_level_node.append(node.left)
                if node.right:
                    current_level_node.append(node.right)
            queue = current_level_node
        return max_level, min_level


if __name__ == '__main__':
    node = Node(3,
                Node(9, None, None),
                Node(20,
                     Node(15,
                          None,
                          Node(4, None, None)
                          ),
                     Node(7, None, None)
                     )
                )
    s = Solution()
    print(s.dfs(node))
    print(s.bfs(node))
