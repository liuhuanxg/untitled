#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 24.两两交换链表中的节点-中等.py
Created Time: 2024/8/13 23:29
"""

"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]

示例 2：
输入：head = []
输出：[]

示例 3：
输入：head = [1]
输出：[1]
 
提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        node0 = dummy = ListNode(next=head)  # 用哨兵节点简化代码逻辑
        node1 = head
        while node1 and node1.next:  # 至少有两个节点
            node2 = node1.next
            node3 = node2.next

            node0.next = node2  # 0 -> 2
            node2.next = node1  # 2 -> 1
            node1.next = node3  # 1 -> 3

            node0 = node1  # 下一轮交换，0 是 1
            node1 = node3  # 下一轮交换，1 是 3
        return dummy.next  # 返回新链表的头节点


if __name__ == '__main__':
    s = Solution()
    ret = s.swapPairs(ListNode(2, ListNode(1)))
    while ret:
        print(ret.val)
        ret = ret.next
