#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 19.删除链表的倒数第N个结点.py
Created Time: 2024/8/13 00:10
"""
"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]
 
提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

进阶：尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        # step1: 获取链表长度
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next

        # step2: 找到倒数第N个节点的前面一个节点
        cur = dummy
        for _ in range(length - n):
            cur = cur.next

        # step3: 删除节点，并重新连接
        cur.next = cur.next.next
        return dummy.next



if __name__ == '__main__':
    s = Solution()
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(s.removeNthFromEnd(node, 2).val)
