#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 200.岛屿的个数.py
给定一个二维数组，1表示陆地，0表示水，问地图中一共有多少个岛屿

方法：
1. DFS或BFS，染色：遍历所有的节点：if node=='1',
                        count++，将node及附近所有的都置为0
                    else：
                        pass
2. 并查集：
    a. 初始化，针对所有为"1"的结点，将元素的parent指向为自己
    b. 遍历所有的结点，将所有相邻的结点合并，1尝试合并，0直接越过。
    c. 遍历查询总共有多少个parents，集合的个数就为最后的答案
"""


class Solution():

    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def num_is_lands(self, grid):
        if not grid or not grid[0]:
            return 0

        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.grid = grid
        self.visited = set()
        return sum(self.flood_fill_dfs(i, j) for i in range(self.max_x) for j in range(self.max_y))

    def flood_fill_dfs(self, x, y):
        """
        深度优先搜索
        :param x:
        :param y:
        :return:
        """
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        for k in range(4):
            self.flood_fill_dfs(x + self.dx[k], y + self.dy[k])
        return 1

    def _is_valid(self, x, y):
        """
        判断元素是否符合
        :param x:
        :param y:
        :return:
        """
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        if self.grid[x][y] == 0 or ((x, y) in self.visited):
            return False
        return True

    def flood_fill_bfs(self, x, y):
        """
        深度优先遍历，判断所有的元素是否合法
        :param x:
        :param y:
        :return:
        """
        if not self._is_valid(x, y):
            return
        self.visited.add((x, y))

        queue = [(x, y)]
        while queue:
            cur_x, cur_y = queue.pop()
            for i in range(4):
                new_x, new_y = cur_x + self.dx[i], cur_y + self.dy[i]
                if self._is_valid(new_x, new_y):
                    self.visited.add((new_x, new_y))
                    queue.append((new_x, new_y))

if __name__ == '__main__':
    arr = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1],
    ]
    s = Solution()
    print(s.num_is_lands(arr))
