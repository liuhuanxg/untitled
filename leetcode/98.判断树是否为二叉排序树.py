#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 98.判断树是否为二叉排序树.py

1. 前序遍历：根左右
2. 中序遍历：左根右
3. 后序遍历：左右根


示例：
输入：[3,1,5,null,null,2]
输出：true

输入：[5,1,4,null,null,3,6]
输出：false

"""


class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Tree():
    def __init__(self, node):
        self.root = node

def main():
    pass


if __name__ == '__main__':
    t = Tree(Node(5, Node(1, None, Node(2, None, None)), Node(3, None, None)))

    main()
