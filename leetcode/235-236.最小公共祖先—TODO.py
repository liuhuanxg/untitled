#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 235-236.最小公共祖先.py

给定两个结点，得到最近公共祖先



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
    def start_check(self, node, value1, value2):
        node1, value1 = self.find_parent(node, value1)
        print(node1, value1)
        node2, value2 = self.find_parent(node, value2)
        print(node2, value2)
        while value1 != value2:
            node1, value1 = self.find_parent(node1, value1)
            node2, value2 = self.find_parent(node2, value2)
        return value1

    def find_parent(self, node, val):
        if node and node.left:
            if node.left.val == val:
                return node, node.val
            return self.find_parent(node.left, val)

        if node and node.right:
            if node.right.val == val:
                return node, node.val
            return self.find_parent(node.right, val)
        return None, None

if __name__ == '__main__':
    node = Node(5,
                Node(1,
                     Node(4,
                          None,
                          None),
                     Node(2,
                          None,
                          None)),
                Node(3,
                     None,
                     None)
                )
    s = Solution()
    # print(s.find_parent(node, 4))
    print(s.start_check(node, 1, 3))
