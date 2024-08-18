#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File Name: 25.K.py
Created Time: 2024/8/14 20:49
"""

"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 
示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

示例 2：
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]
 

提示：
链表中的节点数目为 n
1 <= k <= n <= 5000
0 <= Node.val <= 1000
 

进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseOneGroup(self, head):
        """
        1>2>3
        3>2>1
        :param head:
        :return:
        """
        new_head = None
        while head:
            pre = head.next
            head.next = new_head
            new_head = head
            head = pre

        return new_head

    def reverseKGroup(self, head, k):
        # 统计节点个数
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        p0 = dummy = ListNode(next=head)
        pre = None
        cur = head

        # k 个一组处理
        while n >= k:
            n -= k
            # 先翻转这k个，cur即为这k个翻转之后的
            for _ in range(k):
                nxt = cur.next
                cur.next = pre  # 每次循环只修改一个 next，方便大家理解
                pre = cur
                cur = nxt

            nxt = p0.next
            nxt.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next

    def reverseGroup(self, head):
        cur = dum = ListNode(0)
        while head:
            cur.next = head
            head = head.next
            cur = cur.next
        return dum.next


if __name__ == '__main__':
    s = Solution()
    # s.reverseKGroup()
    # ret = s.reverseOneGroup(ListNode(1, ListNode(2, ListNode(3))))
    ret = s.reverseKGroup(ListNode(1, ListNode(2, ListNode(3))), 2)
    print("===========")
    while ret:
        print(ret.val)
        ret = ret.next
    # ret = s.reverseGroup(ListNode(1, ListNode(2, ListNode(3))))
    # while ret:
    #     print(ret.val)
    #     ret = ret.next
