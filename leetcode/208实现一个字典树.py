#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 208实现一个字典树.py

实现一个字典树，包含以下方法：
insert
search
startsSith

trie.insert("apple")  True
trie.search("apple")  True
trie.insert("app")  False
trie.startsWith("app")  True
trie.insert("app")  True
trie.search("app")  True

"""


class Solution():
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word
        return True

    def search(self, word):
        node = self.root
        for char in word:
            node = node.get(char, {})
        return self.end_of_word in node

    def startsWith(self, word):
        node = self.root
        for char in word:
            if char not in word:
                return False
            node = node[char]
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.insert("apple"))
    print(s.search("apple"))
    print(s.search("app"))
    print(s.startsWith("app"))
    print(s.insert("app"))
    print(s.search("app"))
