#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import OrderedDict


class Solution():
    def __init__(self, capacity):
        self.dic = OrderedDict()
        self.remain = capacity

    def put(self, key, value):
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
            self.dic[key] = value

    def get(self, key):
        if key not in self.dic:
            return -1
        v = self.dic.pop(key)
        self.dic[key] = v
        return v

    def show_value(self):
        return self.dic


if __name__ == '__main__':
    s = Solution(5)
    print(s.get(1))
    print(s.show_value())
    print(s.put(2, 2))
    print(s.put(3, 3))
    print(s.put(4, 4))
    print(s.put(5, 5))
    print(s.put(6, 6))
    print(s.show_value())
    print(s.put(7, 7))
    print(s.show_value())
