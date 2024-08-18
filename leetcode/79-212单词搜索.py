#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 79-212单词搜索.py

给定单词，判断单词是否在二维数组中存在
例：
words = [oath, pea, eat, ran]

Board = [
    [o,a,a,n],
    [e,t,a,e],
    [i,h,k,v],
    [i,f,l,v],
]
1. DFS，每次深度遍历候选词
2. 将所有的词项存在trie中

"""
import collections

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
END_OF_WORD = "#"


class Solution():
    def findWords(self, board, words):
        if not board or not board[0]:
            return []
        if not words:
            return []

        self.results = set()
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD

        self.m, self.n = len(board), len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)

    def _dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_OF_WORD in cur_dict:
            self.results.add(cur_word)

        tmp, board[i][j] = board[i][j], "@"

        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y <= self.n and board[x][y] != "@" and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][i] = tmp


if __name__ == '__main__':
    s = Solution()
