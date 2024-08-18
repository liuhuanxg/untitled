#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: demo3.py
Created Time: 2024/5/13 17:51
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverse_list(self, head):
        new_head = None
        while head:
            last = head.next
            head.next = new_head
            new_head = head
            head = last
        return new_head


if __name__ == '__main__':
    s = Solution()
    ret = s.reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))
    while ret:
        print(ret.val)
        ret = ret.next
