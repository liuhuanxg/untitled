#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: union_find.py
python实现一个并查集
并查集主要用于查找和合并

Find：确定元素属于哪一个子集。它可以被用来确定两个元素是否属于同一个子集
union：将两个子集合并为同一个集合。

"""


class UnionFind():
    def __init__(self, parent):
        self.parent = parent


def makeset(x):
    x.parent = x


def find(x):
    # 查找parent
    if x.parent == x:
        return x
    else:
        return find(x.parent)


def union(x, y):
    xroot = find(x)
    yroot = find(y)
    xroot.parent = yroot


if __name__ == '__main__':
    union_find = UnionFind(3)
    print(find(union_find))
